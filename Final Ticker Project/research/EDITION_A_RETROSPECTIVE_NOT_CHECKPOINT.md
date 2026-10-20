# Edition A

**David Zarate · AI in Finance · October 19, 2026**

*A retrospective reflection on my lab progression, drafted with AI from my saved work and my account of how my AI use changed. Valuation figures are historical lab outputs. This is a new reflection, not the original Edition A checkpoint.*

My progress in AI in Finance has been gradual. I began by using basic financial knowledge and a broad understanding of economic conditions to identify Elevance Health (ELV) as a company worth investigating. Over successive labs, I learned to connect that initial investment idea to cash-flow forecasts, comparable-company analysis, linked pro forma statements, and sensitivity testing. At the same time, I became more careful about how I used AI. Early on, I relied on its answers without consistently checking the facts or mathematics. As the labs progressed, I started using Python to make calculations reproducible, examining assumptions, and questioning whether an output actually supported my conclusion. Each lab added another layer of responsibility to my role as the analyst.

**Early research and Lab 4: Finding an interesting company**

My initial approach was relatively simple: find a company that appeared to offer attractive returns without excessive risk. ELV emerged from a screen that considered factors such as valuation, insider buying, business quality, cash generation, and recovery potential. My macroeconomic thinking was also basic. I considered the broader economic and policy environment through healthcare-cost pressures and government-program exposure, but I had not yet translated those concerns into a detailed financial forecast.

Lab 4 helped me organize that initial idea. Its nine-factor screen forced me to consider unfavorable evidence alongside attractive characteristics. Insider purchases and positive earnings could support further research, while declining membership and pressure on profitability weakened the case for investing immediately. My perspective began to shift from collecting reasons to like ELV toward identifying what would have to improve for the investment thesis to work.

At this stage, I was still inclined to use AI as my brain. I let it do too much of the interpretation and did not consistently verify factual accuracy or mathematical correctness myself. A detailed answer with sources could feel convincing before I had worked through it. Looking back, the structured screen was useful, but having a structured AI answer was only the beginning of understanding the company. The watch-defer conclusion gave me a research direction rather than a finished investment case. [Lab 4](LAB%204.md)

**Lab 5: Moving from a company story to cash-flow valuation**

Lab 5 changed the question I was asking. Instead of focusing mainly on whether ELV looked attractive, I began asking what one share was worth based on future cash flows and what growth the market price already assumed. The first-pass discounted cash-flow analysis produced a value of approximately $375.44 per share under its stated assumptions. More useful than that particular number was learning how projected free cash flow, the discount rate, terminal growth, debt, and available liquidity contributed to the result.

This was an early step toward more advanced financial analysis, but I was still relying heavily on assumptions supplied through the AI interaction. Python also entered my workflow here. The saved lab includes a teaching script with sample inputs, separate from the ELV valuation. That distinction matters: using code did not immediately mean I had independently verified the company analysis. It began moving the mathematics into something visible and repeatable, while leaving me with the responsibility to understand whether the inputs and formulas were appropriate. [Lab 5](Lab%205.md)

**Lab 6: Understanding what had to be true**

Lab 6 made me more skeptical of a precise valuation. The expanded ELV model produced a base estimate of $537.84 per share, but raising the weighted-average cost of capital by one percentage point lowered the estimate to $415.09 with terminal growth unchanged. That result showed me how much the investment conclusion depended on assumptions. The increase from the earlier lab's estimate also did not establish that ELV had become more valuable; the models used different inputs and assumptions.

My macroeconomic thinking became more specific here. Interest rates entered the analysis through the risk-free rate and estimated financing costs. I could see how a higher required return reduced the present value of future cash flows. This connected the broader economic environment to an actual valuation mechanism. I also began separating management guidance, reported historical cash flow, and my forecast assumptions rather than treating them as equally certain.

My use of AI developed along the same lines. I was moving toward asking it to expose the calculation and explain the assumption behind a number. The Python model made it possible to rerun the analysis and change an input. I began to understand that checking the arithmetic and checking the economic reasoning were separate tasks: a calculation can be correct while its forecast remains too optimistic. [Lab 6](lab-06-elv.md)

**Lab 7: Learning that comparisons require judgment**

Lab 7 introduced a different way to challenge a valuation through price-to-earnings multiples. The numerical exercise used Asbury Automotive Group (ABG), which helped me practice the method before applying it to ELV. I learned that selecting comparable companies requires a reasoned policy. Companies do not become useful peers simply because their multiples produce an appealing answer.

The peer-removal exercise added another layer to my analysis. Removing one company changed the implied value, showing that the result depended on who was included. This encouraged me to think more carefully about business mix, growth, and risk before transferring a market multiple. It also gave Python a more deliberate role in my work: calculating the effect of a controlled change and checking how the method behaved when evidence became limited. AI could help implement the comparison, but I still needed to explain why the comparison made sense. [Lab 7](lab-07-elv.md)

**Lab 8: Questioning agreement between models**

Lab 8 applied peer analysis to ELV using UnitedHealth and Cigna as qualified comparisons. The peer-median estimate of $529.58 was close to the saved DCF estimate of $537.84. Earlier in the course, I might have taken that similarity as strong confirmation. By this point, I was learning to inspect what produced the agreement.

Removing UnitedHealth left a Cigna-based estimate of $319.28. The companies also differed in their business mix and earnings quality. I therefore had to consider whether the central estimate was dependable and whether reported earnings represented sustainable profitability. The lab's independent arithmetic check reinforced the value of recomputing results instead of accepting the displayed output.

This was another step in changing my relationship with AI. I could use it to generate criticism, inspect definitions, and help check calculations. I was becoming more comfortable challenging its conclusions and leaving a question unresolved when the evidence was weak. Two similar answers no longer removed the need to understand either answer. [Lab 8](lab-08-elv.md)

**Lab 9: Explaining where free cash flow comes from**

Lab 9 moved my financial analysis into linked pro forma statements. The required ABG exercise and the ELV extension connected the income statement, balance sheet, and cash-flow statement across five forecast years. This made the analysis more demanding because revenue growth and profitability now had consequences for receivables, operating liabilities, investment, financing, and cash balances.

My perspective changed from projecting free cash flow directly to explaining how operations generated it. More revenue could increase earnings while also requiring additional working capital. Capital expenditures consumed cash, and financing choices affected the cash available to shareholders. I also became more attentive to the distinction between free cash flow to the firm and free cash flow to equity, including the appropriate discount rate and treatment of debt.

For my AI use, the major advance was seeing validation become part of the model itself. The work included statement reconciliation and a deliberately broken cash balance that the model rejected. A program producing an answer was no longer sufficient; I wanted evidence that it could identify an inconsistency. Python was becoming a tool for checking financial relationships as well as performing arithmetic. [Lab 9](lab-09-elv.md)

**Lab 10: Adapting the model to ELV's actual business**

Lab 10 showed me why a financial model has to fit the company. ELV's insurance operations required different accounting relationships from an automobile dealership. Medical claims payable belonged among operating liabilities and were linked to benefit expense. The work also replaced an earlier depreciation proxy with a direct filing-based measure, producing a revised illustrative value of $365.24 per opening share.

This connected my earlier economic concerns to more detailed financial assumptions. Medical-cost pressure and premium repricing now affected the margin path and projected cash generation. The model did not independently forecast economy-wide inflation, but it gave me a way to examine how cost and pricing assumptions could affect ELV's statements. I also saw why revenue growth alone was insufficient: the historical record showed revenue increasing while operating cash flow declined.

My approach to AI became more focused on definitions and traceability. I wanted to know what a number measured, where it came from, and why it belonged in a particular formula. Using Python to do my own math increasingly meant working with explicit calculations I could inspect and rerun, even when AI helped generate the code. It also meant recognizing limits: balanced statements did not establish that all consolidated insurance cash was available to shareholders. [Lab 10](lab-10-elv.md)

**Lab 11: Testing the drivers separately**

Lab 11 developed my ability to explain cause and effect. The sensitivity analysis changed revenue growth and margins separately while holding the other independent assumptions at their base settings. Over the tested ranges, growth produced the larger operating-profit span, while margin produced the larger free-cash-flow-to-equity and value-per-share spans.

That result challenged a simple assumption that faster growth must always be the strongest source of value. Growth also increased working-capital needs, so a larger improvement in earnings did not automatically produce a larger improvement in cash flow. I had to follow the effect through the statements to understand the outcome.

This was a further progression in AI use. Rather than asking only for a description of the most important driver, I could use controlled Python calculations to examine the question. Restoring the base case and checking that other inputs stayed fixed made the comparison more trustworthy. I also learned to qualify the conclusion: the driver ranking applied to the ranges tested, not to every possible economic scenario. [Lab 11](Lab11_elv-operating-sensitivity.md)

**Lab 12: Using disagreement to guide research**

Lab 12's discussion of Tesla and ELV helped me consider how different business models and investment needs complicate forecasts. For my own work, the contrast between the saved $537.84 DCF estimate and the $365.24 pro forma-based valuation became especially useful. These models used different dates, assumptions, and valuation conventions, so the gap required investigation before drawing a conclusion.

Earlier, I might have preferred the estimate that best supported my original interest in ELV. By this stage, I was more willing to ask why the models disagreed. That directed attention toward cash conversion, margins, reinvestment, and discounting assumptions. Keeping the watch-defer conclusion reflected a more demanding standard of evidence, even though the decision itself had not changed.

AI was increasingly useful as a discussion partner for identifying questions and organizing competing explanations. The interpretation remained my responsibility. Its ability to explain either result persuasively could not decide which assumptions deserved confidence. [Lab 12](Lab12_discussion.md)

**Lab 13: Connecting correct calculations to the investor's objective**

Lab 13 broadened my perspective from company valuation to portfolio suitability. A portfolio invested entirely in cash passed the exercise's five allocation checks, yet there was no return analysis supporting its ability to meet the objective of CPI plus 4% after costs. This demonstrated that satisfying programmed rules does not establish that a portfolio fulfills its purpose.

My macroeconomic thinking expanded accordingly. Inflation became part of the investor's required outcome: the portfolio needed to support purchasing power as well as meet liquidity and allocation constraints. That required a broader judgment than checking whether weights added to 100%.

This lab also clarified the role I now want AI to play. It can help classify requirements, build a checker, and calculate whether constraints are satisfied. I still have to decide whether those checks address the actual investment question. My development across the labs has therefore been a series of smaller advances: organizing evidence, questioning forecasts, verifying mathematics, tracing statement relationships, testing assumptions, and evaluating the decision those calculations are meant to support. I increasingly use AI as a tool within that process, while taking ownership of the reasoning myself. [Lab 13](lab-13/lab-13-response.md)
