import {defineStore} from "pinia";
import type {EventDTO} from "~/dto/event";
import type {ActorDTO} from "~/dto/actor";

export const useActorStore = defineStore('main', () => {
    const actors = ref<ActorDTO[]>([])
    function increment() {
        count.value++
    }

    return { events }
})