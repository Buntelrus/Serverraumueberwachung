<template>
  <div>
    <navigation/>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
    <p>{{ store.events.length }}</p>
  </div>
</template>

<script setup lang="ts">
import {useEventStore} from "~/stores/event";

const store = useEventStore()
store.loadEvents()
</script>