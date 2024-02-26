<template>
  <div>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
    <input type="text" v-model="message" @keydown.enter="ws.send(message)">
    <div class="messages">
      <p v-for="message in messages">{{ message}}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
const message = ref<string>('')
const messages = ref<string[]>([])
const ws = new WebSocket(`ws://localhost:8000/ws`);
ws.onmessage = event => messages.value.push(event.data)
</script>