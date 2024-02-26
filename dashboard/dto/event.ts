type EventNames = 'person-enter' | 'person-leave';
type Severity = 'critical' | 'warning' | 'info';

interface Event {
    actor: number
    data: any
}

interface ExtendedEvent extends Event {
    name: EventNames
    severity: Severity
}

export type EventDTO = Event | ExtendedEvent;