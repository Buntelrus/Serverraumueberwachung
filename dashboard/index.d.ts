declare module 'nuxt/schema' {
    interface PublicRuntimeConfig {
        secureProtocols: boolean,
        host: string,
        port: number
    }
}
// It is always important to ensure you import/export something when augmenting a type
export {}