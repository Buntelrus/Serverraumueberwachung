import {defineStore} from "pinia";
import type {EventDTO} from "~/dto/event";
import type {ActorDTO} from "~/dto/actor";


export const useEventStore = defineStore('main', () => {
    const ws = new WebSocket(`ws://localhost:8000/ws`)
    const events = ref<EventDTO[]>([])
    ws.onmessage = event => events.value.push(event.data)
    ws.onopen = () => {
        console.log('open')
        ws.send('nice its open')
    }
    async function loadEvents() {
        events.value = await $fetch<EventDTO[]>(`http://localhost:8000/events`)
    }

    return { events, loadEvents }
})