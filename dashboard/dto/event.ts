// type EventNames = 'person-enter' | 'person-leave';
// type Severity = 'critical' | 'warning' | 'info';

export interface EventDTO {
    device: number
    data: any
}

// interface ExtendedEvent extends Event {
//     name: EventNames
//     severity: Severity
// }
//
// export type EventDTO = Event | ExtendedEvent;