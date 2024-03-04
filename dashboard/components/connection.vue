<template>
  <div class="connection" :class="{connected}">
    {{ connected ? 'Connection established' : 'No Connection'}}
  </div>
</template>

<script setup lang="ts">
  import {useWebsocket} from "~/composables/websocket";
  import {useEventListener} from "~/composables/event-listener";

  const ws = useWebsocket()
  const connected = ref<boolean>(ws.readyState === ws.OPEN)
  useEventListener(ws, 'open', () => {
    connected.value = true
  })
  useEventListener(ws, 'close', () => {
    connected.value = false
  })
</script>

<style lang="sass">
  .connection
    width: 100%
    height: 3rem
    background: var(--error)

    &.connected
      background: var(--success)

</style>
