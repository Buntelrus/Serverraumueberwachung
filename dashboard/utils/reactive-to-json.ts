import {type Ref, toValue} from "vue";

export const refsToJson = (data: Record<string, Ref>) => {
    const rawData: any = {}
    for (const key in data) {
        rawData[key] = toValue(data[key])
    }
    return JSON.stringify(rawData)
}