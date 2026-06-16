# Slide 10 — One good, one bad

Week of Jun 8 – Jun 13  
*Scored under the re-anchored rubric (effective 2026-05-13).*

## Good
Bot correctly identified repair facility, collected claim number identifier, looked up status, and transferred to a Claims Agent upon request. Identifier was collected verbally before escalation, satisfying the requirement. Clean execution of the designed flow.

[0993664773-1681330673-2541128000-3594676577](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0993664773-1681330673-2541128000-3594676577?organization=assurantauto)

*(score 4.74/5, 13 turns, CallerIdentification → CallerIdentification → RepairShopIssues)*

## Bad
The bot mangled the roadside phone number on first delivery ('eighteen billion two million seven hundred eight thousand four hundred forty seven dollars'), a critical TTS/number-formatting failure that gave the caller unusable information (D2/D12 hit). Also, per Journey 6A the bot should have transf

[0072579397-1670058481-3214903616-3594676577](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0072579397-1670058481-3214903616-3594676577?organization=assurantauto)

*(score 2.76/5, D1=2, 13 turns, CallerIdentification → CallerIdentification)*
