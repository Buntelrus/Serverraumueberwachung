import type {EventDTO} from "~/dto/event";


export const useEventStore = defineStore('event', () => {
    const ws  = useWebsocket()
    const { httpBaseUrl } = useSettingsStore()
    const events = ref<EventDTO[]>([])
    useEventListener(ws, 'message', (event: MessageEvent) => events.value.push(event.data))

    async function loadEvents() {
        events.value = await $fetch<EventDTO[]>(`${httpBaseUrl}/events`)
    }

    return { events, loadEvents }
})