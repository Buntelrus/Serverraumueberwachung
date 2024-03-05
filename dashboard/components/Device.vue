<template>
  <article>
    <h2>{{ device.name }}</h2>
    <p v-if="!short">{{ device.description }}</p>
    <slot>value: {{ device.value }}</slot>
  </article>
</template>

<script setup lang="ts">
  import type {DeviceDTO} from "~/dto/device";

  const short = false
  // todo: withDefaults -> show description true
  const { device } = defineProps<{
    device: DeviceDTO
  }>()
</script>
