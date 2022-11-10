$(document).ready(function() {$('#calendar').evoCalendar({ theme: 'Midnight Blue', calendarEvents: [
{id: '0', name: 'DIY', date:'2022/12/31', description: 'location later', type:'https://support.researchautism.org/DIY2022'},
{id: '1', name: 'Chevron Houston Marathon & Half Marathon', date:'2023/01/15', description: 'location later', type:'https://support.researchautism.org/2023-houston-marathon'},
{id: '2', name: 'TCS London Marathon', date:'2023/04/23', description: 'location later', type:'https://support.researchautism.org/2023london'},
{id: '3', name: 'Big Sur International Marathon', date:'2023/04/30', description: 'location later', type:'https://support.researchautism.org/BigSur2023'},
{id: '4', name: 'Dicks Sporting Goods Pittsburgh Marathon', date:'2023/05/07', description: 'location later', type:'https://support.researchautism.org/Pitt2023'},
{id: '5', name: 'Escape from Alcatraz Triathlon', date:'2023/06/11', description: 'location later', type:'https://support.researchautism.org/alcatraz2023'},
{id: '6', name: 'BMW Berlin Marathon', date:'2023/09/24', description: 'location later', type:'https://support.researchautism.org/berlin2023'},
{id: '7', name: 'Bank of America Chicago Marathon', date:'2023/10/08', description: 'location later', type:'https://support.researchautism.org/Chicago2023'},
{id: '8', name: 'Irish Life Dublin Marathon', date:'2023/10/29', description: 'location later', type:'https://support.researchautism.org/Dublin2023'},
{id: '9', name: 'DIY', date:'2023/12/31', description: 'location later', type:'https://support.researchautism.org/DIY2023'},
]});$('#calendar').on('selectEvent', function(event,activeEvent) {window.open(activeEvent.type); })});