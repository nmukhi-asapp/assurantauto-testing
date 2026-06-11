# Slide 10 — One good, one bad

Week of Jun 1 – Jun 7  
*Scored under the re-anchored rubric (effective 2026-05-13).*

## Good
Bot correctly identified caller, recovered from initial ANI lookup failure by collecting alternate identifier, looked up contract, and resolved the request by texting the Vehicle Care Plan portal link. Clean execution end-to-end with no observable defects.

[2076060016-1589842417-2188820981-1773867395](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2076060016-1589842417-2188820981-1773867395?organization=assurantauto)

*(score 4.80/5, 21 turns, CallerIdentification → CallerIdentification → ContractHolderIssues)*

## Bad
Caller's speech is highly disfluent/unintelligible and ASR is clearly struggling (D10=2). Bot failed to recover or escalate after repeated breakdowns — should have transferred to a live agent rather than looping with 'rephrase' prompts (D1=2, D6=2). Bot also asked for a phone number after the ANI lo

[4258187493-1589776881-2356250944-3594676577](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4258187493-1589776881-2356250944-3594676577?organization=assurantauto)

*(score 3.18/5, D1=2, 18 turns, CallerIdentification → CallerIdentification → ContractHolderIssues)*
