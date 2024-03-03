import {defineStore} from "pinia";
import {refsToJson} from "~/utils/reactive-to-json";
import type {PublicRuntimeConfig} from "@nuxt/schema";

interface Settings {
    secureProtocols: PublicRuntimeConfig['secureProtocols'],
    host: PublicRuntimeConfig['host'],
    port: PublicRuntimeConfig['port']
}

const LOCAL_STORAGE_KEY = 'settings'

export const useSettingsStore = defineStore('main', () => {
    const runtimeConfig = useRuntimeConfig()

    const secureProtocols = ref(runtimeConfig.public.secureProtocols)
    const host = ref(runtimeConfig.public.host)
    const port = ref(runtimeConfig.public.port)

    const httpBaseUrl = computed(() => `${secureProtocols.value ? 'https' : 'http'}://${host.value}:${port.value}`)
    const wsBaseUrl = computed(() => `${secureProtocols.value ? 'wss' : 'ws'}://${host.value}:${port.value}`)

    loadSettings()
    function loadSettings() {
        const settings: Settings | any = parseSettings()
        console.log(settings)
        if (settings.secureProtocols) secureProtocols.value = settings.secureProtocols
        if (settings.host) host.value = settings.host
        if (settings.port) port.value = settings.port
    }

    console.log('secure', secureProtocols.value)
    console.log('host', host.value)
    console.log('port', port.value)
    function saveSettings() {
        localStorage.setItem(LOCAL_STORAGE_KEY, refsToJson({ secureProtocols, host, port }))
    }
    return { secureProtocols,host, port, loadSettings, saveSettings, httpBaseUrl, wsBaseUrl }
})

function parseSettings(): {} | Settings {
    try {
        return JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY) || "{}")
    } catch (err) {
        console.error('failed to parse settings', err)
        localStorage.removeItem(LOCAL_STORAGE_KEY)
        return {}
    }
}