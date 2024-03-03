export const useTestConnection = () => {
    const { httpBaseUrl } = useSettingsStore()
    return $fetch(httpBaseUrl)
}