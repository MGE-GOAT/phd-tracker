"""make_batch3.py -- adds batch 3 (broader, mostly easier groups) to data/plan.json and writes their emails into emails/.
Germany details come from the verified August 2026 sweep (~/Documents/phd-germany/targets-ranked.csv); NL and Austria from the 22 Nov 2026 searches."""
import csv, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.expanduser("~/Documents/phd-germany/targets-ranked.csv")
url = {r["rank"]: r["url"] for r in csv.DictReader(open(CSV))}

THESIS = ("My thesis is an always-on voice assistant for older adults. I designed a 75k-parameter wake-word model, trained it with int8 "
          "quantization-aware training and run it in real time on a Raspberry Pi. Under five-fold cross-validation on held-out recordings and unseen "
          "speakers it was the most accurate model on every fold against DS-CNN, TC-ResNet8, BC-ResNet and DS-CNNs matched to its size and compute. "
          "In deployment the device microphone tripled false alarms while AUC barely moved, and retraining on hard negatives recorded on the device "
          "cut false activations from 60 to 3 in a 388-hour test.")
PAPERS = ("This work has produced a system paper accepted at ICBME 2026 (IEEE), a compact-model paper submitted to ICEE 2027 and a journal paper "
          "submitted to IEEE Sensors Journal. I also work as an embedded and ML systems engineer. My CV is attached and my code is at github.com/MGE-GOAT.")
SIG = "Kind regards,\nMahrad Ghazli\nMSc Biomedical Engineering, Sharif University of Technology\nmge.goat@gmail.com"

# id, country, who, where, page, address, why (for the page), hook (for the email), topic (subject), match, chance, greet
T = [
 ("hein","Germany","Prof. Andreas Hein","University of Oldenburg, assistive systems",url["10"],"","Elderly care, fall detection and assistive living, your thesis topic exactly.","Your group's work on ambient assisted living, fall detection and supporting caregivers is exactly the setting of my thesis.","assistive health technology for older adults",10,6,"Prof. Hein"),
 ("offis","Germany","OFFIS Health division","Oldenburg, PhD with University of Oldenburg",url["12"],"","In-home fall detection with automatic emergency calls, the same product you built.","Your in-home fall detection work with automatic emergency calls is the same kind of system I built and deployed.","in-home emergency detection",9,6,"OFFIS Health team"),
 ("strodthoff","Germany","Prof. Nils Strodthoff","University of Oldenburg, AI4Health","https://uol.de/en/ai4health","","Deep learning on ECG and biosignals, BME plus ML.","Your group's deep-learning work on ECG and other physiological signals is where I would like to take my embedded ML experience.","deep learning for physiological signals",8,6,"Prof. Strodthoff"),
 ("kirste","Germany","Prof. Thomas Kirste","University of Rostock",url["27"],"","Activity recognition and emergency detection for assisted living.","Your chair's work on activity recognition and emergency detection for ambient assisted living matches the system I built for older adults.","activity recognition for assisted living",8,6,"Prof. Kirste"),
 ("otte","Germany","Prof. Sebastian Otte","University of Lübeck, Adaptive AI",url["35"],"","AI that keeps learning under tight energy and memory limits.","Your group's focus on AI that keeps learning under tight energy, memory and compute limits is the problem I met after deploying my model.","adaptive AI under resource limits",8,6,"Prof. Otte"),
 ("grzegorzek","Germany","Prof. Marcin Grzegorzek","University of Lübeck, Medical Informatics",url["33"],"","Wearable and multimodal health sensing.","Your institute's work on wearable sensing and signal quality in health monitoring is close to what my thesis taught me about sensors.","wearable health sensing",7,6,"Prof. Grzegorzek"),
 ("bringmann","Germany","Prof. Oliver Bringmann","University of Tübingen, Embedded Systems",url["18"],"","Ultra-low-power audio AI and medical edge computing.","Your chair's work on co-optimising neural networks and hardware for ultra-low-power audio and medical edge computing is the next step from my thesis.","low-power audio AI on embedded hardware",9,5,"Prof. Bringmann"),
 ("froening","Germany","Prof. Holger Fröning","Heidelberg University, HAWAII Lab",url["25"],"","Quantisation and int8 deployment, exactly your skills.","Your lab's work on quantisation-aware training, int8 deployment and compilers for embedded inference is exactly what I have been doing in practice.","quantised embedded inference",9,5,"Prof. Fröning"),
 ("idmt","Germany","Fraunhofer IDMT, Hearing, Speech and Audio","Oldenburg, PhD with University of Oldenburg",url["2"],"","Speech recognition in real products, values shipped code.","Your institute's work on speech recognition and acoustic monitoring for real products is what I have done on a small device.","speech technology on devices",9,5,"Hearing, Speech and Audio Technology team"),
 ("maier","Germany","Prof. Andreas Maier","FAU Erlangen, Pattern Recognition Lab",url["37"],"","Clinical speech analysis and medical AI, very large lab.","Your lab's work on clinical speech analysis and medical time series is a natural continuation of my speech work.","clinical speech and medical AI",8,5,"Prof. Maier"),
 ("empkins","Germany","EmpkinS research centre (Prof. Martin Vossiek)","FAU Erlangen",url["22"],"","Getting human health state out of imperfect physical sensors.","EmpkinS's focus on extracting human state from imperfect physical sensors is the lesson my thesis taught me with a microphone.","health sensing from imperfect sensors",8,5,"Prof. Vossiek"),
 ("arnrich","Germany","Prof. Bert Arnrich","HPI Potsdam, Digital Health",url["32"],"","Health sensing outside the clinic.","Your chair's work on sensing health outside the clinic is the setting my device was built for.","ubiquitous health sensing",8,5,"Prof. Arnrich"),
 ("lukowicz","Germany","Prof. Paul Lukowicz","DFKI Kaiserslautern, Embedded Intelligence",url["42"],"","Wearables and energy-efficient sensing systems, very international.","Your department's work on wearable sensing and energy-efficient context-aware systems is where my embedded ML experience fits best.","wearable embedded intelligence",8,5,"Prof. Lukowicz"),
 ("kolossa","Germany","Prof. Dorothea Kolossa","TU Berlin, Electronic Systems of Medical Engineering",url["40"],"","Robust speech recognition and medical electronic systems.","Your group's work on speech recognition in adverse conditions and on medical electronic systems matches both halves of my background.","robust speech recognition",8,5,"Prof. Kolossa"),
 ("schuller_tum","Germany","Prof. Björn Schuller","TUM, Health Informatics",url["14"],"","Computer audition for health, competitive.","Your chair's work on computer audition for health in real-world settings is where I would like to take my audio work.","computer audition for health",8,4,"Prof. Schuller"),
 ("martin","Germany","Prof. Rainer Martin","Ruhr University Bochum, Communication Acoustics",url["39"],"ika-office@ruhr-uni-bochum.de","Hearing devices and low-complexity speech processing.","Your institute's work on hearing devices and low-complexity speech processing matches my experience running speech models on small hardware.","low-complexity speech processing",7,5,"Prof. Martin"),
 ("haeb","Germany","Prof. Reinhold Haeb-Umbach","Paderborn University, Communications Engineering",url["49"],"","Robust speech recognition.","Your department's work on robust speech recognition is close to my wake-word research.","robust speech recognition",7,5,"Prof. Haeb-Umbach"),
 ("durmaz","Netherlands","Prof. Özlem Durmaz-Incel","University of Twente, Pervasive Systems","https://www.utwente.nl/en/eemcs/ps/","ozlem.durmaz@utwente.nl","Distributed embedded AI and sensing, the group is growing.","Your group's work on collaborative embedded sensing and distributed embedded AI, from device to edge, is exactly where my experience sits.","embedded AI for sensing systems",9,5,"Prof. Durmaz-Incel"),
 ("qingwang","Netherlands","Dr. Qing Wang","TU Delft, Embedded AI lab","https://www.google.com/search?q=Qing+Wang+TU+Delft+Embedded+AI+lab","","Low-bit networks on microcontrollers, coordinates an EU embedded-AI doctoral network.","Your lab's work on low-bit networks and running models on microcontrollers is what my int8 wake-word work does on a Raspberry Pi.","low-bit models on microcontrollers",9,4,"Dr. Wang"),
 ("tejedor","Netherlands","Dr. Cristian Tejedor Garcia","Radboud University, voice diagnostics","https://www.ru.nl/en/research/research-news/ngf-ained-fellowship-grant-for-research-into-voice-diagnostics","","Speech AI for diagnosing disease, grant for several PhDs.","Your project on responsible AI for voice diagnostics is the health speech direction I would like to work in.","speech AI for health diagnostics",8,5,"Dr. Tejedor Garcia"),
 ("stuijk","Netherlands","Prof. Sander Stuijk / Prof. Henk Corporaal","TU Eindhoven, Electronic Systems","https://www.tue.nl/onderzoek/researchers/sander-stuijk","","Efficient edge AI processing.","Your group's work on efficient processing at the edge, where data must stay on the device, matches my privacy-first device design.","efficient edge AI",7,4,"Prof. Stuijk"),
 ("rinner","Austria","Prof. Bernhard Rinner","University of Klagenfurt, Networked and Embedded Systems","https://nes.aau.at/","bernhard.rinner@aau.at","Embedded and pervasive systems, often hiring PhDs.","Your group's work on networked and embedded sensing systems is where my embedded ML experience fits.","embedded sensing systems",7,5,"Prof. Rinner"),
 ("aral","Austria","Asst. Prof. Atakan Aral","University of Vienna, edge AI and IoT","https://sc.cs.univie.ac.at/news-events/open-positions","","Edge AI, federated learning and IoT, has hired PhDs on this.","Your group's work on edge AI, federated learning and IoT is close to what I built, a device that keeps its data local.","edge AI and IoT",8,5,"Dr. Aral"),
 ("pro2future","Austria","Pro2Future (PhD with TU Graz)","Graz","https://www.pro2future.at/?p=15170","jobs@pro2future.at","Embedded AI PhD in a research centre, some adverts ask for good German.","Your PhD position in cognitive products and embedded AI matches my embedded ML background.","embedded AI",7,5,"Pro2Future team"),
]

def email(t):
    _, country, who, where, page, addr, why, hook, topic, m, c, greet = t
    return (f"To: {addr or '(address on ' + page + ')'}\nSubject: Prospective PhD student in {topic} (MSc Sharif University)\n\n"
            f"Dear {greet},\n\nI am finishing my MSc in Biomedical Engineering at Sharif University of Technology, and I would like to ask whether you "
            f"have or expect a funded PhD position{'' if 'team' in greet else ' in your group'}.\n\n{hook} {THESIS}\n\n{PAPERS}\n\n"
            f"If a position might open, I would be glad to apply.\n\n{SIG}\n")

plan = json.load(open(os.path.join(ROOT, "data/plan.json")))
plan["steps"] = [s for s in plan["steps"] if s["batch"] in (1, 2)]
for t in T:
    sid = t[0]
    open(os.path.join(ROOT, "emails", f"email_{sid}.txt"), "w").write(email(t))
    plan["steps"].append({"id": sid, "batch": 3, "country": t[1], "who": t[2], "where": t[3], "why": t[6], "kind": "Email", "page": t[4],
                          "email": f"email_{sid}.txt", **({"address": t[5]} if t[5] else {}), "match": t[9], "chance": t[10]})
json.dump(plan, open(os.path.join(ROOT, "data/plan.json"), "w"), indent=1, ensure_ascii=False)
print(len(plan["steps"]), "steps")
