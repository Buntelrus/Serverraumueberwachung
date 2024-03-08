<template>
  <div>
    <h1>Settings</h1>
    <form @submit.prevent="tryConnectionAndSaveSettings">
      <label for="secure-protocols"></label>
      <input id="secure-protocols" type="checkbox" v-model="settings.secureProtocols">
      <label for="host"></label>
      <input id="host" type="text" v-model="settings.host">
      <label for="port"></label>
      <input id="port" type="number" v-model="settings.port">
      <button type="submit">Speichern</button>
    </form>
    <div v-if="error" class="error">
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import {useTestConnection} from "~/composables/test-connection";

const router = useRouter()
const cameFrom = router.options.history.state.back
const settings = useSettingsStore()
const { connectToWebsocket } = useWebsocket()

const error = ref<string|undefined>(undefined)
const tryConnectionAndSaveSettings = () => useTestConnection()
    .then(() => {
      connectToWebsocket()
      settings.saveSettings()
      router.push(cameFrom as string || '/')
    })
    .catch(err => {
      error.value = err
    })

</script>