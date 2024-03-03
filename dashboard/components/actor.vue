<template>
  <div class="actor">
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
    <slot>value: {{ value }}</slot>
  </div>
</template>

<script setup lang="ts">
  const {title, description, value} = defineProps<{
    title: string,
    description: string,
    value: any
  }>()
</script>
