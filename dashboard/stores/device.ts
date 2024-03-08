import {defineStore} from "pinia";
import type {DeviceDTO} from "~/dto/device";

export const useDeviceStore = defineStore('device', () => {
    const { httpBaseUrl } = useSettingsStore()
    const devices = ref<DeviceDTO[]>([])

    const temperatureDevice = computed(() => devices.value.find(device => device.name === 'temperature'))
    const personCountDevice = computed(() => devices.value.find(device => device.name === 'person-counter'))
    async function loadDevices() {
        devices.value = await $fetch<DeviceDTO[]>(`${httpBaseUrl}/devices`)
    }

    return { devices, loadDevices, temperatureDevice, personCountDevice }
})