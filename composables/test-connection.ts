import type {EventDTO} from "../dashboard/dto/event";

export const useTestConnection = () => {
    return $fetch(`http://localhost:8000/`)
}