import {defineStore} from "pinia";
import type {EventDTO} from "~/dto/event";
import {useWebsocket} from "../../composables/websocket";
import {useEventListener} from "../../composables/event-listener";


export const useEventStore = defineStore('main', () => {
    const ws  = useWebsocket()
    const events = ref<EventDTO[]>([])
    useEventListener(ws, 'message', (event: MessageEvent) => events.value.push(event.data))

    async function loadEvents() {
        events.value = await $fetch<EventDTO[]>(`http://localhost:8000/events`)
    }

    return { events, loadEvents }
})