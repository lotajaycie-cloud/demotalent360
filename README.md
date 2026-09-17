# Talent 360 — Demo Build

A demonstration build of Talent 360 for Century Pacific Group. **This build contains
no employee data.** Every person, rating, development plan and successor nomination in
it is synthetic, generated for demonstration purposes only.

Open `index.html` in a browser. No build step, no server, no dependencies.

## Sign in

Passcode for every account: `demo2026`

| Sign in as | Email | Sees |
| --- | --- | --- |
| Super Admin | `cogayon@centurypacific.com.ph` | The whole databank, all 8 business units |
| Super Admin | `wsranes@centurypacific.com.ph` | The whole databank, all 8 business units |
| HR Business Partner | `eabalos@centurypacific.com.ph` | Only assigned business units, never their own record |
| GM / Exec | `bbarretto@centurypacific.com.ph` | Their whole company, every department below |
| People Manager | `aortega@centurypacific.com.ph` | Direct reports only |
| Employee | `mlagdameo@centurypacific.com.ph` | Their own record and development plan |

Any employee number in the dataset also works as a sign-in ID.

## What's in the synthetic dataset

| | |
| --- | --- |
| People | 100 talents, plus 2 super admins |
| In the 2026 cycle | 85 |
| Placed on the 9-box | 74 |
| Competency ratings | 57 talents, 13 drivers each |
| Development actions | 73 IDP, 26 8-quarter |
| Critical roles | 20 |
| Successor nominations | 27 |
| Business units | 8, across 3 HR business partners |

## How the names were made

Given names, middle names and surnames were drawn at random from pools of common
Philippine names and recombined. No name was taken from an employee record. Any
resemblance to a real person is coincidental. Employee numbers start at 900001 and
do not correspond to any real numbering.

## Scope of this build

This is a demonstration of the interface and the reporting logic. It is not a
production system:

- Access control runs in the browser, not on a server
- The passcode is in the page source
- The full dataset ships inside the page

Those limits are acceptable here precisely because the data is invented. They are
not acceptable for a build carrying real employee data, which is what the production
version needs a server, SSO and a database for.

## Files

```
index.html        the whole application, single file
gen_demo.py       generator that produced the synthetic dataset
demo_t360.json    the generated payload, as embedded in index.html
```

## Regenerating the data

```bash
python3 gen_demo.py     # writes demo_t360.json
```

The generator is seeded, so it reproduces the same dataset each run. Change the seed
at the top of the file for a different population.
