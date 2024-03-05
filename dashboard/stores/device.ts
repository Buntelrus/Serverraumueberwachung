import {defineStore} from "pinia";
import type {DeviceDTO} from "~/dto/device";

export const useDeviceStore = defineStore('device', () => {
    const { httpBaseUrl } = useSettingsStore()
    const devices = ref<DeviceDTO[]>([])

    async function loadDevices() {
        devices.value = await $fetch<DeviceDTO[]>(`${httpBaseUrl}/devices`)
    }

    return { devices, loadDevices }
})