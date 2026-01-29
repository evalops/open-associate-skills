# Liquidation waterfall model: [Company]

## Cap table summary (pre-round)

| Class | Shares | % ownership | Investment | Liq pref | Participation | Seniority |
|---|---|---|---|---|---|---|
| Series A | | | $3m | 1x | Non-part | Pari passu |
| Seed | | | $1.5m | 1x | Non-part | Pari passu |
| SAFEs | (converts) | | $500k | (converts) | | |
| Common | | | N/A | None | Pro rata | Last |
| Option pool | | 10% | N/A | None | Pro rata | Last |
| **Total** | | 100% | | | | |

## New round terms

| Term | Value |
|---|---|
| Round | Series B |
| Investment | $10m |
| Pre-money | $40m |
| Post-money | $50m |
| New investor % | 20% |
| Liq pref multiple | 1x |
| Participation | Participating |
| Participation cap | 3x |
| Seniority | Senior to all |

## Liquidation stack (pay order)

1. **Series B** - $10m preference, participating to 3x cap ($30m max)
2. **Series A + Seed** - $4.5m combined preference, non-participating (choose higher of pref or conversion)
3. **Common** - Pro rata of remainder

## Waterfall scenarios

### Scenario 1: $10m exit (acqui-hire)

| Step | Description | Amount | Remaining |
|---|---|---|---|
| Start | Exit proceeds | $10m | $10m |
| 1 | Series B preference (1x) | $10m | $0 |
| 2 | Series A preference | $0 | $0 |
| 3 | Seed preference | $0 | $0 |
| 4 | Common | $0 | $0 |

| Class | Payout | % of exit | Multiple on investment |
|---|---|---|---|
| Series B | $10m | 100% | 1.0x |
| Series A | $0 | 0% | 0x |
| Seed | $0 | 0% | 0x |
| Common/Founders | $0 | 0% | N/A |

### Scenario 2: $30m exit (modest outcome)

| Step | Description | Amount | Remaining |
|---|---|---|---|
| Start | Exit proceeds | $30m | $30m |
| 1 | Series B preference (1x) | $10m | $20m |
| 2a | Series A preference (1x) | $3m | $17m |
| 2b | Seed preference (1x) | $1.5m | $15.5m |
| 3 | Series B participation (20% of $15.5m) | $3.1m | $12.4m |
| 4 | Series A conversion check: $12.4m × 15% = $1.86m < $3m, stays with pref | $0 | $12.4m |
| 5 | Seed conversion check: $12.4m × 7.5% = $0.93m < $1.5m, stays with pref | $0 | $12.4m |
| 6 | Common (57.5% of remainder) | $7.13m | $5.27m |
| 7 | Series B additional participation (capped) | Already counted | |

| Class | Payout | % of exit | Multiple on investment |
|---|---|---|---|
| Series B | $13.1m | 43.7% | 1.31x |
| Series A | $3m | 10% | 1.0x |
| Seed | $1.5m | 5% | 1.0x |
| Common/Founders | $12.4m | 41.3% | N/A |

### Scenario 3: $100m exit (good outcome)

| Step | Description | Amount | Remaining |
|---|---|---|---|
| Start | Exit proceeds | $100m | $100m |
| 1 | Series B preference (1x) | $10m | $90m |
| 2 | Series B participation (20% of $90m = $18m, but capped at 3x = $30m total) | $20m | $70m |
| 3 | Series A conversion: $70m × 15% = $10.5m > $3m pref, converts | $10.5m | $59.5m |
| 4 | Seed conversion: $59.5m × 7.5% = $4.46m > $1.5m pref, converts | $4.46m | $55.04m |
| 5 | Common (57.5%) | $31.65m | $23.39m |

Wait, need to recalculate with proper pro-rata after Series B hits cap...

**Corrected calculation:**
- Series B hits $30m cap (3x), gets no more participation
- Remaining $70m split pro rata among Series A, Seed, Common
- Series A: 15% → $10.5m
- Seed: 7.5% → $5.25m  
- Common: 57.5% → $40.25m
- (Series B already got $30m)

| Class | Payout | % of exit | Multiple on investment |
|---|---|---|---|
| Series B | $30m | 30% | 3.0x (at cap) |
| Series A | $10.5m | 10.5% | 3.5x |
| Seed | $5.25m | 5.25% | 3.5x |
| Common/Founders | $54.25m | 54.25% | N/A |

### Scenario 4: $500m exit (great outcome)

At large exits, all preferred converts to common and shares pro rata.

| Class | Ownership % | Payout | Multiple |
|---|---|---|---|
| Series B | 20% | $100m | 10x |
| Series A | 15% | $75m | 25x |
| Seed | 7.5% | $37.5m | 25x |
| Common/Founders | 57.5% | $287.5m | N/A |

## Summary table

| Exit | Series B | Series A | Seed | Founders | Founder % |
|---|---|---|---|---|---|
| $10m | $10m | $0 | $0 | $0 | 0% |
| $30m | $13.1m | $3m | $1.5m | $12.4m | 41% |
| $100m | $30m | $10.5m | $5.25m | $54.25m | 54% |
| $500m | $100m | $75m | $37.5m | $287.5m | 58% |

## Key insights

1. **Below $14.5m exit:** Series B takes everything (preference stack exceeds exit value)
2. **$14.5m - $50m exits:** Participation hurts founders significantly
3. **Above $50m:** Series B hits 3x cap, founder % improves
4. **Above $100m:** All preferred converts, standard pro rata

## Negotiation notes

- The 3x participation cap saves founders at large exits
- Without the cap, Series B would take $20m + participation at $100m exit
- Non-participating would be better for founders at $30-50m exits
- Push for non-participating OR lower participation cap (2x)
