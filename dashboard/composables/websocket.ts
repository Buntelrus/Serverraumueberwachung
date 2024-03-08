let ws: WebSocket
let interval: NodeJS.Timeout
let timeout: NodeJS.Timeout
const retryInterval = 30
const retryInSeconds = ref<number|undefined>(undefined)
const eventListeners: any[] = []
const connectionEstablished = ref<boolean|null>(false)
const connectToWebsocket = () => {
    if (connectionEstablished.value !== false) return
    connectionEstablished.value = null
    clearInterval(interval)
    clearTimeout(timeout)
    retryInSeconds.value = retryInterval
    const { wsBaseUrl } = useSettingsStore()
    ws = new WebSocket(`${wsBaseUrl}/ws`)
    for (const args of eventListeners) {
        ws.addEventListener.apply(ws, args as any)
    }
    ws.addEventListener('open', () => {
        console.log('open')
        connectionEstablished.value = true
    })
    ws.addEventListener('close', () => {
        console.log('close')
        connectionEstablished.value = false
        interval = setInterval(() => retryInSeconds.value!--, 1000)
        timeout = setTimeout(() => {
            connectToWebsocket()
            clearInterval(interval)
        }, retryInterval * 1000)

    })
    ws.addEventListener('error', err => {
        console.log('error', err)
    })
}
export const useWebsocket = () => {
    connectToWebsocket()
    const websocket = new Proxy<WebSocket>(ws, {
        get(target, prop, receiver) {
            switch (prop) {
                case 'addEventListener': return (...args: any[]) => {
                    eventListeners.push(args)
                    ws.addEventListener.apply(ws, args as any)
                }
                case 'removeEventListener': return (...args: any[]) => {
                    const index = eventListeners.findIndex(item => {
                        for (const i in item) {
                            if (args[i as keyof typeof args] !== item[i]) {
                                return false
                            }
                        }
                        return true
                    })
                    eventListeners.splice(index, 1)
                    ws.removeEventListener.apply(ws, args as any)
                }
                default: return target[prop as keyof typeof target]
            }
        },
    })

    return { ws: websocket, connectToWebsocket, connectionEstablished, retryInSeconds }
}