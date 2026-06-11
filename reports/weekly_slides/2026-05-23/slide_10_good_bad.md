# Slide 10 — One good, one bad

Week of May 18 – May 23  
*Scored under the re-anchored rubric (effective 2026-05-13).*

## Good
Bot correctly handled a coverage/claim initiation question for a contract holder, providing accurate guidance and the claims phone number. Main weakness is D9 verbosity — responses were script-y and long, particularly the initial coverage rundown and the final phone-number turn that bundled selling-

[2822538112-1405358577-3156197877-1773867395](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2822538112-1405358577-3156197877-1773867395?organization=assurantauto)

*(score 4.56/5, 23 turns, CallerIdentification → CallerIdentification → ContractHolderIssues)*

## Bad
Bot collected a VIN identifier from the caller, failed lookup, then asked for the identifier AGAIN before transfer and ultimately ended the call instead of transferring despite repeated explicit agent requests — a critical D1 failure (refused to escalate when required, caller stuck in loop and aband

[0700046509-1390285297-2857273664-3594676577](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0700046509-1390285297-2857273664-3594676577?organization=assurantauto)

*(score 2.62/5, D1=1, 32 turns, CallerIdentification → CallerIdentification → RepairShopIssues)*
