export interface DeviceDTO {
    id: number
    name: string
    description: string
    value: boolean | { temperature: number, humidity: number }
}