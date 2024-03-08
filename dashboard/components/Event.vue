<template>
  <article :class="event.severity">
    <h2 v-if="eventTitle">{{ eventTitle }}</h2>
    <span class="device-id">{{ event.device }}</span>
    <span class="device-value">{{ event.data }}</span>
  </article>
</template>

<script setup lang="ts">
  import type {EventDTO} from "~/dto/event";

  const eventNameMap = {
    'person-enter': "Person entered!",
    'person-leave': "Person left!"
  }

  const eventTitle = computed(() => event.name && eventNameMap[event.name as keyof typeof eventNameMap])
  const { event } = defineProps<{
    event: EventDTO
  }>()
</script>
