<template>
  <section class="device-list">
    <Device v-for="device in deviceStore.devices" :device="device"/>
  </section>
</template>
<script setup lang="ts">
  const deviceStore = useDeviceStore()
</script>