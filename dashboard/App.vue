<template>
  <section class="connection">
    <Connection/>
  </section>
  <section class="navigation">
    <Navigation/>
  </section>
  <NuxtLayout>
    <NuxtPage/>
  </NuxtLayout>
</template>

<script setup lang="ts">
import {useTestConnection} from "~/composables/test-connection";

const router = useRouter()
useTestConnection().catch(() => router.push('/settings'))
const eventStore = useEventStore()
const deviceStore = useDeviceStore()
console.log(eventStore)
eventStore.loadEvents()
deviceStore.loadDevices()
</script>

<style lang="sass">
@use "sass/main"
</style>