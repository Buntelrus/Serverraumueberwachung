<template>
  <section class="device-list">
    <Event v-for="event in eventStore.events" :event="event"/>
  </section>
</template>
<script setup lang="ts">
  const eventStore = useEventStore()
</script>