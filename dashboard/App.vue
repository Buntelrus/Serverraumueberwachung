<template>
  <div>
    <connection/>
    <navigation/>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
    <p>{{ eventStore.events.length }}</p>
  </div>
</template>

<script setup lang="ts">
import {useTestConnection} from "~/composables/test-connection";

const router = useRouter()
useTestConnection().catch(() => router.push('/settings'))
const eventStore = useEventStore()
console.log(eventStore)
eventStore.loadEvents()
</script>