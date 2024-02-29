let ws: WebSocket
const eventListeners: any[] = []
const connectToWebsocket = () => {
    ws = new WebSocket(`ws://localhost:8000/ws`)
    for (const args of eventListeners) {
        ws.addEventListener.apply(ws, args as any)
    }
    ws.addEventListener('open', () => {
        console.log('open')
    })
    ws.addEventListener('close', () => {
        console.log('close')
        retry()
    })
    ws.addEventListener('error', err => {
        console.log('error', err)
    })
}
const retry = () => setTimeout(connectToWebsocket, 3000)
connectToWebsocket()
export const useWebsocket = () => {
    return new Proxy<WebSocket>(ws, {
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
}