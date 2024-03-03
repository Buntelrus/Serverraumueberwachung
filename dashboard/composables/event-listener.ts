export const useEventListener = (target: EventTarget, event: string, callback: (event: any) => void) => {
    // if you want, you can also make this
    // support selector strings as target
    onMounted(() => target.addEventListener(event, callback))
    onUnmounted(() => target.removeEventListener(event, callback))
}