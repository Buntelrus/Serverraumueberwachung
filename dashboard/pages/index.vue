<template>
  <div>
    <h1>Serverraum Dashboard</h1>
    <DeviceList />
    <EventList />
  </div>
</template>

<script setup lang="ts">
import type {EventDTO} from "~/dto/event";

const { ws } = useWebsocket()

const deviceStore = useDeviceStore()

const temperature = computed({
  get() {
    return deviceStore.temperatureDevice?.value.temperature
  },
  set(value) {
    if (deviceStore.temperatureDevice) {
      deviceStore.temperatureDevice.value.temperature = value
    }
  }
})
const personCount = computed({
  get() {
    return deviceStore.personCountDevice?.value
  },
  set(value) {
    if (deviceStore.temperatureDevice) {
      deviceStore.temperatureDevice.value = value
    }
  }
})

useEventListener(ws,'message', (event: EventDTO) => {
  // temperature update
  // person count update
})
</script>