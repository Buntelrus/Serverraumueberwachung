<template>
  <div>
    <connection/>
    <navigation/>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
    <p>{{ store.events.length }}</p>
  </div>
</template>

<script setup lang="ts">
import {useTestConnection} from "../composables/test-connection";

const router = useRouter()
useTestConnection().catch(() => router.push('/settings'))
const store = useEventStore()
store.loadEvents()
</script>