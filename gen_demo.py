# -*- coding: utf-8 -*-
"""Builds a 100-person synthetic T360 payload with the exact shape of the real one.
Names are randomly recombined from common Philippine given-name and surname pools;
they are not drawn from any employee record."""
import json, random
random.seed(360)

GIVEN_M = ["JOSE","ANTONIO","RAMON","MIGUEL","CARLO","ENRIQUE","FERNANDO","RAFAEL","EDUARDO","NOEL",
           "ARNEL","DENNIS","ROLANDO","GERARDO","MARVIN","JOEL","PATRICIO","ALFONSO","REYNALDO","BENJAMIN",
           "IGNACIO","LEANDRO","TEODORO","VICENTE","HERMINIO"]
GIVEN_F = ["MARIA","ANGELA","CRISTINA","ROSARIO","LORNA","IMELDA","PATRICIA","TERESITA","JOSEFINA","CARMEN",
           "DIVINA","LUISA","MARGARITA","CONCEPCION","BEATRIZ","AURORA","ESPERANZA","VICTORIA","CLARISSA","MILAGROS",
           "REGINA","SOLEDAD","FELICIDAD","NARCISA","PAZ"]
MID = ["BAUTISTA","REYES","SANTOS","CRUZ","GARCIA","MENDOZA","TORRES","FLORES","RAMOS","AQUINO",
       "DELA PENA","VILLANUEVA","NAVARRO","SALAZAR","ESTRADA","PANGANIBAN","MAGSAYSAY","OCAMPO","LIM","TAN"]
SUR = ["ABALOS","BERNABE","CABRERA","DALISAY","ENRIQUEZ","FAJARDO","GALANG","HIZON","IBANEZ","JAVIER",
       "KATIGBAK","LAGDAMEO","MANALO","NEPOMUCENO","OBLIGACION","PALAFOX","QUIAMBAO","RIVERA","SUMULONG","TIANGCO",
       "UMALI","VELASCO","WENCESLAO","YAPTINCHAY","ZAMORA","ARELLANO","BUENAVENTURA","CORPUZ","DIZON","ESPIRITU",
       "FERRER","GUEVARRA","HERNANDEZ","INOCENCIO","JUGO","LAUREL","MACAPAGAL","NOLASCO","ORTEGA","PRIETO",
       "QUINTOS","ROXAS","SORIANO","TUAZON","URBANO","VERGARA","YULO","ZARAGOZA","ALMONTE","BARRETTO"]

BU = ["Domestic Sales","Global Brands","Foodservice & Food Solutions","Supply Chain & Logistics",
      "Corporate Finance","Corporate Human Resources","Research & Development","Digital Business Solutions"]
BU_COMPANY = {"Domestic Sales":"CPFI","Global Brands":"CPFI","Foodservice & Food Solutions":"CPFI",
              "Supply Chain & Logistics":"GTC","Corporate Finance":"CPFI","Corporate Human Resources":"CPFI",
              "Research & Development":"GTC","Digital Business Solutions":"CPAVI"}
DEPT = {"Domestic Sales":"DOMESTIC SALES","Global Brands":"GLOBAL BRANDS",
        "Foodservice & Food Solutions":"FOODSERVICE","Supply Chain & Logistics":"SUPPLY CHAIN AND LOGISTICS",
        "Corporate Finance":"CORPORATE FINANCE","Corporate Human Resources":"CORPORATE HR",
        "Research & Development":"RESEARCH AND DEVELOPMENT","Digital Business Solutions":"DIGITAL BUSINESS SOLUTIONS"}
DIV = {"Domestic Sales":"COMMERCIAL","Global Brands":"COMMERCIAL","Foodservice & Food Solutions":"COMMERCIAL",
       "Supply Chain & Logistics":"OPERATIONS","Corporate Finance":"CORPORATE","Corporate Human Resources":"CORPORATE",
       "Research & Development":"OPERATIONS","Digital Business Solutions":"CORPORATE"}

TITLES = {
 "EXEC":["VICE PRESIDENT","ASSISTANT VICE PRESIDENT","GENERAL MANAGER"],
 "DM":["DEPARTMENT MANAGER","SENIOR DEPARTMENT MANAGER","GROUP MANAGER"],
 "SM":["SECTION MANAGER","SENIOR SECTION MANAGER","ASSISTANT MANAGER"],
 "SUP":["SUPERVISOR","SENIOR SUPERVISOR","TEAM LEAD"],
 "RF":["ANALYST","SPECIALIST","ASSOCIATE","COORDINATOR"],
}
LVL   = ["EXEC","DM","SM","SUP","RF"]
COMPS = ["BIAS FOR ACTION","BIG PICTURE THINKING","COMMUNICATION","DRIVE AND AMBITION","EMOTIONAL INTELLIGENCE",
         "FORWARD THINKING, OPPORTUNITY-SEEKING, AND INNOVATING","FUNCTIONAL EXCELLENCE","LEADING PEOPLE",
         "LEARNING AND CHANGE AGILITY","MAKING SOUND JUDGMENT","PLANNING AND EXECUTION",
         "STAKEHOLDER MANAGEMENT","UNDERSTANDING THE BUSINESS"]
SEC   = ["BEHAVIOR","APTITUDE","BEHAVIOR","CAPACITY TO LEAD","BEHAVIOR","CAPACITY TO LEAD","APTITUDE",
         "CAPACITY TO LEAD","APTITUDE","APTITUDE","CAPACITY TO LEAD","BEHAVIOR","APTITUDE"]
TIERS = ["Emergency Cover","Ready Now","Ready 1-2 Years","Ready 2-3 Years","Ready 3-5 Years"]
LEARN = ["Classroom training","Coaching","Mentoring","On-the-job assignment","Job rotation","Special project",
         "External seminar","Certification","Self-study","Cross-functional exposure"]
STATUS= ["Done","Ongoing","Behind","Not Yet Started","Deferred","On-Going/On-Track","DONE"]
TARGET= ["31-Mar-2026","30-Jun-2026","30-Sep-2026","31-Dec-2026","31-Mar-2027","30-Jun-2027"]
ACTIONS = [
 "Lead the quarterly category review and present findings to the leadership team",
 "Complete a supervisory skills programme and apply the feedback model with the team",
 "Shadow the planning cycle end to end and document the handover points",
 "Take ownership of one cross-functional project with a named sponsor",
 "Run a monthly coaching conversation with each direct report",
 "Build and present a three-year capability plan for the section",
 "Rotate into a partner department for one full planning cycle",
 "Complete a data analysis certification and rebuild one recurring report",
 "Facilitate the team's goal-setting workshop for the coming cycle",
 "Represent the department in the monthly business review",
 "Draft the standard operating procedure for the new process and train the team on it",
 "Mentor two junior colleagues through their first full cycle",
 "Lead a continuous improvement initiative with a measurable target",
 "Complete the finance-for-non-finance programme and apply it to the unit budget",
 "Present a customer insight study to the commercial leadership group",
]
STRAT = ["BUILD","BUY","BOOST"]

def idx(lst, v):
    if v not in lst: lst.append(v)
    return lst.index(v)

pos_l, lvl_l, dept_l, div_l, comp_l = [], [], [], [], []
learn_l, partner_l, status_l, target_l = [], [], [], []
for l in LVL: idx(lvl_l, l)

used_names = set()
def make_name():
    while True:
        sur = random.choice(SUR)
        if random.random() < .5: giv = random.choice(GIVEN_M)
        else: giv = random.choice(GIVEN_F)
        nm = "%s, %s %s" % (sur, giv, random.choice(MID))
        if nm not in used_names:
            used_names.add(nm); return nm

def handle(name):
    sur, rest = name.split(", ")
    return (rest.split(" ")[0][0] + sur.split(" ")[0]).lower().replace("-", "")

# ---- headcount plan: 100 talents + 2 super admins ------------------------
PLAN = [("EXEC",6),("DM",18),("SM",34),("SUP",30),("RF",12)]
people, rows = [], []
emp_seq = 900100

def new_emp():
    global emp_seq
    emp_seq += 1
    return str(emp_seq)

handles = {}
for lvl, n in PLAN:
    for _ in range(n):
        bu = random.choice(BU)
        nm = make_name()
        h = handle(nm)
        while h in handles: h = h + str(random.randint(2, 9))
        handles[h] = True
        people.append({"empNo": new_emp(), "name": nm, "lvl": lvl, "bu": bu, "handle": h,
                       "title": random.choice(TITLES[lvl]) + " - " + DEPT[bu]})

# reporting lines: each level reports to someone one step up in the same BU
by_lvl_bu = {}
for p in people: by_lvl_bu.setdefault((p["lvl"], p["bu"]), []).append(p)
for p in people:
    up = LVL[max(0, LVL.index(p["lvl"]) - 1)]
    cands = by_lvl_bu.get((up, p["bu"])) or by_lvl_bu.get(("DM", p["bu"])) or []
    cands = [c for c in cands if c["empNo"] != p["empNo"]]
    p["mgr"] = random.choice(cands)["empNo"] if cands else 0

# cycle membership, boxes, ratings
BOXES = [1,2,3,4,5,6,7,8,9]
PERF  = {1:"Low",2:"Med",3:"High",4:"Low",5:"Med",6:"High",7:"Low",8:"Med",9:"High"}
POT   = {1:"Low",2:"Low",3:"Low",4:"Med",5:"Med",6:"Med",7:"High",8:"High",9:"High"}
for p in people:
    p["tr2026"] = random.random() < .85
    p["box"] = random.choices(BOXES, weights=[2,4,6,5,14,12,4,11,8])[0] if (p["tr2026"] and random.random() < .90) else 0
    p["box2025"] = random.choice(BOXES) if (p["box"] and random.random() < .6) else 0
    p["risk"] = random.choices([0,1,2,3], weights=[52,24,16,8])[0]
    p["age"] = random.randint(27, 58)
    p["tenure"] = round(random.uniform(1.2, 24.0), 1)

for p in people:
    rows.append([p["empNo"], p["name"],
                 idx(pos_l, p["title"]), idx(lvl_l, p["lvl"]),
                 idx(dept_l, DEPT[p["bu"]]), idx(div_l, DIV[p["bu"]]),
                 idx(comp_l, BU_COMPANY[p["bu"]]), p["mgr"],
                 p["age"], p["tenure"], p["handle"],
                 p["box"], PERF.get(p["box"], ""), POT.get(p["box"], ""),
                 p["risk"], p["box2025"], 1, 1 if p["tr2026"] else 0,
                 BU.index(p["bu"])])

# ---- super admins --------------------------------------------------------
ADMINS = [
  {"empNo":"900001","name":"OGAYON, CRIS ARMAND","handle":"cogayon","bu":"Digital Business Solutions",
   "title":"HEAD OF INFORMATION SECURITY AND DATA PRIVACY OFFICE","lvl":"DM"},
  {"empNo":"900002","name":"RANES, W. S.","handle":"wsranes","bu":"Corporate Human Resources",
   "title":"CORPORATE HR DEPARTMENT MANAGER","lvl":"DM"},
]
for a in ADMINS:
    rows.append([a["empNo"], a["name"], idx(pos_l, a["title"]), idx(lvl_l, a["lvl"]),
                 idx(dept_l, DEPT[a["bu"]]), idx(div_l, DIV[a["bu"]]),
                 idx(comp_l, BU_COMPANY[a["bu"]]), 0, 44, 6.0, a["handle"],
                 0, "", "", 0, 0, 1, 0, BU.index(a["bu"])])

# ---- competency ratings --------------------------------------------------
r_rows = []
for p in people:
    if not p["box"] or random.random() > .72: continue
    lean = {7:1.4, 8:1.5, 9:1.7, 6:1.2, 5:1.0, 4:.9, 3:.7, 2:.6, 1:.5}[p["box"]]
    codes = []
    for _ in COMPS:
        if random.random() < .06: codes.append(-1); continue
        v = random.random() * 2 * lean
        codes.append(2 if v > 2.1 else (1 if v > 1.0 else 0))
    r_rows.append([p["empNo"]] + codes)

# ---- development actions -------------------------------------------------
idp_rows, q8_rows = [], []
succ_pool = [p for p in people if p["tr2026"]]
for p in succ_pool:
    if random.random() > .42: continue
    for _ in range(random.randint(1, 4)):
        idp_rows.append([p["empNo"], random.choice(ACTIONS),
                         idx(learn_l, random.choice(LEARN)),
                         idx(partner_l, random.choice(people)["name"]),
                         idx(target_l, random.choice(TARGET)),
                         idx(status_l, random.choice(STATUS)), 0])

# ---- critical roles and successors ---------------------------------------
leaders = [p for p in people if p["lvl"] in ("EXEC", "DM")]
role_rows, succ_rows = [], []
for p in leaders:
    if random.random() > .82: continue
    rid = "r" + p["empNo"]
    role_rows.append([rid, p["empNo"], p["title"], idx(lvl_l, p["lvl"]),
                      idx(dept_l, DEPT[p["bu"]]), idx(div_l, DIV[p["bu"]]),
                      random.choice(STRAT)])
    if random.random() < .72:
        cands = [c for c in people if c["bu"] == p["bu"] and c["lvl"] in ("DM","SM") and c["empNo"] != p["empNo"]]
        random.shuffle(cands)
        for c in cands[:random.randint(1, 3)]:
            succ_rows.append([rid, random.randint(0, 4), c["empNo"]])

# 8-quarter plans belong to named successors
named = sorted({s[2] for s in succ_rows})
for e in named:
    if random.random() > .45: continue
    for _ in range(random.randint(2, 4)):
        q8_rows.append([e, random.choice(ACTIONS),
                        idx(learn_l, random.choice(LEARN)),
                        idx(partner_l, random.choice(people)["name"]),
                        idx(target_l, random.choice(TARGET)),
                        idx(status_l, random.choice(STATUS)), 1])

# ---- HR partners ---------------------------------------------------------
HRBP_SPEC = [("Domestic Sales","Global Brands","Foodservice & Food Solutions"),
             ("Supply Chain & Logistics","Research & Development"),
             ("Corporate Finance","Digital Business Solutions")]
hrbp_rows, bupart = [], [None]*len(BU)
hr_people = [p for p in people if p["bu"] == "Corporate Human Resources" and p["lvl"] in ("DM","SM")]
while len(hr_people) < 3:
    nm = make_name(); h = handle(nm) + "x"
    e = new_emp()
    rows.append([e, nm, idx(pos_l,"HR BUSINESS PARTNER"), idx(lvl_l,"DM"),
                 idx(dept_l,"CORPORATE HR"), idx(div_l,"CORPORATE"), idx(comp_l,"CPFI"),
                 0, 41, 8.0, h, 0, "", "", 0, 0, 1, 0, BU.index("Corporate Human Resources")])
    hr_people.append({"empNo":e,"name":nm,"handle":h,"bu":"Corporate Human Resources","lvl":"DM"})
for i, units in enumerate(HRBP_SPEC):
    hp = hr_people[i]
    talents = [p["empNo"] for p in people if p["bu"] in units]
    hrbp_rows.append([hp["empNo"], hp["name"], hp["handle"],
                      "HR BUSINESS PARTNER", "CORPORATE HR", talents])
    for u in units: bupart[BU.index(u)] = hp["empNo"]
for i, b in enumerate(BU):
    if bupart[i] is None: bupart[i] = "ADMIN"

T = {"pos":pos_l,"lvl":lvl_l,"dept":dept_l,"div":div_l,"comp":comp_l,
     "learn":learn_l,"partner":partner_l,"status":status_l,"target":target_l,
     "comps":COMPS,"sec":SEC,"tiers":TIERS,
     "p":rows,"r":r_rows,"idp":idp_rows,"q8":q8_rows,
     "roles":role_rows,"succ":succ_rows,"hrbp":hrbp_rows,
     "bu":BU,"bupart":bupart}

json.dump(T, open("demo_t360.json","w"), separators=(",", ":"))
print("people        ", len(rows), " (100 talents + 2 super admins + HR partners)")
print("in 2026 cycle ", sum(1 for r in rows if r[17]))
print("placed        ", sum(1 for r in rows if r[11]))
print("rated         ", len(r_rows))
print("IDP actions   ", len(idp_rows), "| 8QTR actions", len(q8_rows))
print("critical roles", len(role_rows), "| successor nominations", len(succ_rows))
print("HR partners   ", len(hrbp_rows), "| business units", len(BU))
