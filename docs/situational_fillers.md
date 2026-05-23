# Situational Fillers — assurantauto (GACS `main`)

Fillers are time-buying phrases the Talker says while waiting for the Reasoner to respond.
Each task defines its own filler table. The Talker is instructed to use phrases **exactly as written** and to **never repeat the same or nearly identical phrase on consecutive turns**.

---

## CallerIdentification

*Source: `talkerPromptOverride`*

| Situation | Example customer turn | Approved phrases |
|---|---|---|
| Caller identified as repair facility or dealership | "Dealer" / "Repair facility" / "Independent" | "Give me a moment while I look up your information." / "One moment while I check on that." |
| Caller identified as contract holder | "Contract Holder" / "Customer" | "Give me a second while I pull up your contract and claims." |
| Customer requested to speak to a human agent | "Talk to someone." / "Speak to a human." / "Connect me with an agent." / "Customer service rep." | "Let me see what I can do for you." / "Let me check the best way to help you." |
| No clear match | — | "One moment please." / "Let me check." / "Just a second." |

---

## ContractHolderIssues

*Source: `voiceCommunicationGuidelines`*

| Situation | Example customer turn | Approved phrases |
|---|---|---|
| Customer stated their opening request | "I need to start a claim" | "Let me check your contract." / "One moment while I look into your contract." / "Let me check on that for you." |
| Customer asked about contract terms, coverage, or eligibility | "Is my engine covered?" / "Car rental" / "How do I get reimbursed?" | "Hmm, give me a sec while I check the relevant policies." / "One moment while I look up your coverage." / "Let me see what your contract says about that." |
| Customer requested to speak to an agent | "I need to speak to a representative" | "One moment." / "Let me see what I can do for you." / "Let me check on the best way to help." |
| Customer answered a question you asked (confirmed info) | "Twenty twenty-two RAV4" | "Got it, one moment." / "Perfect, let me look that up." / "Thanks, give me just a second." |
| Customer explained their issue after a deflection attempt | "I need a whole new engine" | "Let me look into that." / "I'll check on that for you." / "One moment while I look that up." |
| No clear match | — | "One moment please." / "Let me check." / "Just a second." |

---

## RepairShopIssues

*Source: `voiceCommunicationGuidelines`*

| Situation | Example customer turn | Approved phrases |
|---|---|---|
| Customer wants to check a claim | "Claim status." / "Check on a claim." / "Checking status of existing claim." | "One moment while I check on that." / "Let me pull that up for you." / "Give me just a second to check on that claim." |
| Customer wants to file a new claim | "Start a claim." / "New claim." / "I need to file a claim." | "One moment while I get that started." / "Let me check what I need from you." / "Give me a second." |
| Customer asking about payment status | "I need to check a payment status." / "I want to know about the payment status." / "Payment question." | "One moment while I check on that payment." / "Let me pull up the payment details for you." / "Give me a second to look up the payment." |
| Customer provided a claim number, VIN, or case number | "Four nine three nine five eight one five." / "Yeah. The last eight are S P three five seven one six one." | "Got it, one moment." / "Perfect, let me look that up." / "Thanks, give me just a second." |
| Customer confirmed an identifier you read back | "Yes." / "That's correct." / "Yep." / "Correct." | "Thank you, one moment." / "Got it, let me check on that." / "Perfect, just a second." |
| Customer clarified the type of identifier they gave | "Claim number." / "Last eight of the VIN." / "Case number." | "Got it, one moment." / "Understood, let me check that." / "Thanks for clarifying — just a second." |
| Customer described their issue or asked a coverage question | "Claim is taking too long." / "I've got a question about coverage." / "I have a customer's car here and need to know if the labor will be covered." | "Let me look into that for you." / "One moment while I check on that." / "I'll look into that right away." |
| Customer requested to speak to a human agent or adjuster | "Agent, please." / "I need to speak with an adjuster." / "No. Representative." / "Phone agent." | "One moment." / "Let me see what I can do." / "Let me get you connected." |
| Customer declined self-service and chose to wait for a phone agent | "Continue to wait." / "Phone." / "No." | "Understood, one moment." / "Got it, I'll check on that." / "One moment please." |
| Customer confirmed a step in the new-claim process (email sent or case number received) | "I sent it." / "I got it." / "Four nine four one three three one three." | "Perfect, give me just a moment." / "Great, let me pull that up." / "Thanks, let me check the next step." |
| No clear match | — | "One moment please." / "Let me check." / "Just a second." |

---

## DealershipIssues

*Source: `voiceCommunicationGuidelines`*

| Situation | Example customer turn | Approved phrases |
|---|---|---|
| Opening request — checking existing claim | "Existing claim." / "Open claim." / "I need to check a claim status." | "One moment while I pull that up." / "Let me look up that claim for you." / "Give me just a second." |
| Opening request — filing a new claim (phone preferred) | "File a new claim." / "Start a new claim." / "Over the phone." / "Claims adjuster." | "One moment while I connect you with an adjuster." / "Let me get that set up." / "Give me a second." |
| Customer wants to modify or add to an existing claim | "I need to add to the claim." / "Thermostat." / "Labor time." / "Part adjustment." / "I would like to add parts and labor." | "One moment while I pull up that claim." / "Let me check on the existing claim." / "Give me just a second." |
| Customer provided a claim number or VIN | "Claim number is four eight eight two seven six nine nine." / "The last eight of the VIN are K N six eight three three six seven." | "Got it, one moment." / "Perfect, let me look that up." / "Thanks, give me just a second." |
| Customer confirmed an identifier you read back | "Yes." / "That's correct." / "That's right." | "Thank you, one moment." / "Perfect, just a second." / "Got it, let me proceed." |
| Customer clarified the type of identifier they gave | "That is the claim number." / "VIN number." / "Last eight." | "Got it, one moment." / "Understood, let me check that." / "Thanks for clarifying — just a second." |
| Customer asked a coverage or eligibility question | "Coverage question." / "Check for coverage." / "I have a customer waiting and I need approvals now." / "Can it be reopened?" | "One moment while I check the coverage." / "Let me look into that for you." / "Give me a second to check on that." |
| Customer says a check was issued but not received | "Have not received payment." / "I need to check on a payment that hasn't come in." / "Payment." | "One moment while I check on that payment." / "Let me look into the payment status." / "Give me just a second." |
| Customer requested to speak to a human agent | "Talk to someone." / "Speak to a human." / "Connect me with an agent." / "Customer service rep." | "One moment." / "Let me see what I can do." / "Let me get you connected." |
| Customer declined self-service and chose to wait for a phone agent | "No." / "Over the phone." / "Claims adjuster." | "Understood, one moment." / "Got it, I'll get you in the queue." / "One moment please." |
| Customer has a contract or account issue | "I need the contract number." / "Contract issue." | "One moment while I look that up." / "Let me check on that for you." / "Give me just a second." |
| No clear match | — | "One moment please." / "Let me check." / "Just a second." |
