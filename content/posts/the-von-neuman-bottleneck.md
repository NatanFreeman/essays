---
title: "The Von Neuman bottleneck: Why AI 2.0 will live in Israel"
date: 2026-02-05T10:00:00-05:00 # Placeholder date, adjust as needed
draft: true
---
The Von Neuman bottleneck: Why
Al 2.0 will live in Israel
By Natan Freeman

## The Philosophical Failure: Breaking the Von Neumann Bottleneck

There has been sentiment of lament over Israel's supposed failure to invest in
the Al space. "Why isn't there an Israeli ChatGPT?" one might ask. This is
unfair as a lot of the R&D is happening in Israel. Consider NVIDIA's significant
presence in Israel or Google Deepmind's Israeli research team. Not to
mention the work done by universities and startups in this space as well as
the Ministry of Defense's dedicated Al unit. One could argue that ChatGPT is
the Israeli ChatGPT.

But there is some truth to this sentiment. Israel isn't building datacenters to
the same extent as the U.S., and we aren't seeing many foundation models
coming from Israel. But this is not an oversight. Israel is simply looking two
steps ahead. They know they can't directly compete with the U.S. and China
in the current landscape of GPU-dominated large-language-models. So Israel
is building out the infrastructure for the next generation of Al. The one which
will be defined by lower power costs, greater real-time capabilities and more
decentralization in edge and server environments. Israel is building Al 2.0.
The way they will do that is by breaking the Von Neuman bottleneck.

You see there is a glass ceiling to Al which is fundamentally limiting what Al
can do. Whenever we try to incorporate biologically inspired features we hit
this ceiling and fail catastrophically. Attempts to encode episodic memory,
continuous memory, real-time data streaming or efficient processing have
either resulted in low fidelity implementations or inefficiency with our current
hardware. This is not a failure of implementation; it's a failure of philosophy.
You cannot fix a hardware problem with a software solution.

To understand why a hardware revolution is necessary, we must look at the
specific capabilities that Al 2.0 demands-capabilities that are currently
impossible to implement efficiently.

The first is Episodic Memory, or the ability to learn from a single event
instantly. Consider a child touching a hot stove: they do not need to touch it
ten thousand times to understand it is dangerous. They experience it once,
and their neural pathways physically alter to encode that memory forever.
Current Al cannot do this. To "teach" a neural network a new fact, you must
run a massive training pass, updating billions of parameters in a slow, energy-
intensive batch process. If an autonomous drone flies into a new type of
windowpane it hasn't seen before, it cannot simply "remember" that obstacle
for the return trip. It remains frozen in the state it was trained in until a team of
engineers collects the data, relabels it, and retrains the model in a server farm
weeks later. True autonomy requires the ability to learn continuously from a
sample size of one.

This ties directly into the second critical concept: Continuous Learning.
Today's Large Language Models suffer from "catastrophic forgetting." If you
try to teach a pre-trained model a new language or a new medical protocol
without the original training data, it overwrites its previous weights, effectively
forgetting what it used to know. This renders Al systems brittle and static; they
are "frozen brains" trapped in the past. Real-world applications—whether it's a
personalized healthcare assistant tracking a patient's degrading condition
over years, or a missile defense system adapting to a new flight trajectory
mid-air-require a system that can continuously update its understanding of
the world without needing to go offline for a reboot. We need Al that evolves,
not just Al that executes.

Finally, we face the hurdle of Real-Time Data Streaming. We often conflate
"fast" with "real-time," but they are not the same. A GPU is fast because it
processes massive batches of data in parallel, but it has high latency. It waits
to fill a bus with data before crunching the numbers. In contrast, biological
survival depends on processing information as a continuous, noisy stream. A
self-driving car on a highway doesn't have the luxury of batching 50 frames of
video to decide if a pedestrian is stepping out; it needs to process the photon
hitting the sensor immediately. In edge environments, where bandwidth is
nonexistent and decisions must be made in microseconds, the current "store-
then-compute" architecture is simply too slow to survive.

The reason we cannot implement these features today is not a lack of clever
code; it is the Von Neumann bottleneck. In our current architecture, the
processing unit (the brain) and the memory unit (the book) are physically
separated, connected by a narrow bus. Every time the Al wants to "think" or
"learn," it must stop, send a request to memory, drag the data across the wire,
compute it, and send the result back.

When we attempt to implement continuous learning or episodic memory, we
are asking the computer to constantly rewrite its own memory. This triggers a
catastrophic traffic jam. The system spends 90% of its time and energy just
moving data back and forth, rather than doing the actual math. This is the
"Memory Wall." It is why training a model takes months and costs millions; we
are paying for the commute, not the calculation. And this isn't just a problem
for battery-constrained drones. In massive data centers, this data movement
is the primary source of heat. We are hitting a thermodynamic wall where
scaling up current Al models is becoming physically impossible because we
cannot cool the wires fast enough to keep up with the data traffic. To build Al
2.0, we must tear down this wall and build chips where the memory is the
computer.

This is what neuromorphic computing has been preaching for over a decade.
Yet companies in this space have failed to reach mass production. But there
is one country looking to break this barrier. In this essay I will explain exactly
how.

## The Innovator's Dilemma: Why the Giants and Startups Failed
Let us first look at some failures as a test case. Intel's Loihi 3 chip is a key
example.

To be fair, Intel isn't selling vaporware. With the Loihi architecture, they have
successfully demonstrated the immense potential of neuromorphic computing
in tangible, existing applications. They have showcased impressive
benchmarks in adaptive robotics, gesture recognition, and even olfactory
sensing, proving that spiking neural networks can process complex, real-time
data with a fraction of the power budget required by a standard GPU.
Technically speaking, the silicon works.

However, this technical validation is rendered moot by a fatal strategic flaw:
the ecosystem is hermetically sealed. Intel has built a walled garden so high
that it virtually guarantees zero widespread adoption. You cannot simply buy a
Loihi chip off the shelf to integrate into a consumer product, nor can you easily
port existing models to it. Access is largely gatekept behind the Intel
Neuromorphic Research Community (INRC), restricted to cloud-based
simulations or strictly vetted academic partnerships. By forcing developers to
use a proprietary, idiosyncratic software stack rather than integrating
seamlessly with open standards, Intel ensures that their technology remains a
niche curiosity rather than an industry standard.

This refusal to open up is not merely an oversight; it is a calculated hesitation
born of the Innovator's Dilemma. Intel is the reigning emperor of the Von
Neumann architecture. Their entire trillion-dollar legacy, supply chain, and
revenue stream are built on the x86 instruction set-on high-frequency clock
cycles and the distinct separation of memory and processing. To truly
Democratize neuromorphic computing-to make it cheap, accessible, and
interoperable-would be to cannibalize their own core business. Intel cannot
aggressively push a technology that renders their cash cow obsolete. As a
result, they are incentivized to keep neuromorphic computing as an eternal
"science project"-impressive enough to claim innovation, but closed off
enough to ensure it never threatens the dominance of their traditional
processors. It lets them keep a foot in the door without letting anyone else in.
Just in case.

This is the innovator's dilemma, and we expect it from big companies. But
what about the startups, how are they doing?

Consider Mythic Al, a Texas-based startup that became the poster child for
the dangers of this industry.

Mythic didn't just try to tweak the existing paradigm; they tried to shatter the
Von Neumann bottleneck by betting on analog compute-in-memory. Their
premise was brilliant and deeply biologically inspired: instead of shuttling data
back and forth between memory and processors (the exact bottleneck Intel
struggles with), Mythic performed calculations inside the memory arrays
themselves using flash transistors. This mimics the human brain's synapses,
where storage and computation happen in the same place.

On paper, it was revolutionary. They promised the compute power of a
desktop GPU at a fraction of the energy cost, perfect for edge Al. Investors
poured in over $150 million. The industry hype was palpable.

Then, reality hit.

In late 2022, Mythic ran out of cash and nearly collapsed. While they have
since been "resurrected" by a modest funding round, they serve as a
cautionary tale of a "Zombie Unicorn." Their failure wasn't just financial; it was
a failure to scale a new philosophy in a hardware world built for the old one.

Mythic faced two insurmountable walls. First, analog computing is incredibly
noisy. Unlike digital logic, which is a clean 0 or 1, analog signals fluctuate with
temperature and manufacturing variances. Trying to tame this "noise" required
complex compensation algorithms that ate away at the very efficiency gains
they promised.

Second, and more fatal, was the software barrier. Just like Intel, Mythic found
that having a brilliant chip is useless if no one can program it. They had to
build their own software stack from scratch because standard tools like
PyTorch and TensorFlow assume digital, deterministic hardware. Developers,
already stretched thin, didn't have the time to learn an entirely new, esoteric
coding language for a chip that might not exist in a year.

Mythic proved that being "better" isn't enough. You can have the most
biologically accurate chip in the world, but if you cannot manufacture it reliably
or integrate it into the existing software supply chain, you are simply building a
very expensive museum piece.

To enter this space, a startup would have to have full vertical integration.
Everything from the market product, to the software stack and even the
lithographic nodes need to be thought out and developed in a cohesive
ecosystem. This isn't a company – it's an entire industry. And the one place
where this industry is being developed is Israel.

## The Silicon Island: Israel’s Sovereign Vertical Integration
It's natural to draw analogies between Israel's neuromorphic computing
industry and Taiwan's silicon industry from the 1980s. This is by design of
course. Israel has learnt the lessons used to transform Taiwan into the world's
chip giant, and applying it to make Israel the home for Al 2.0. Not just for
industry, but as a matter of national security.

To understand the magnitude of what is happening in Israel, we must first
correct a common misconception about the rise of TSMC. Taiwan
Semiconductor Manufacturing Company was not born from the scrappy
ambition of a garage startup; it was a state-engineered miracle.

In the 1970s and 80s, the Taiwanese government realized they could not
compete with the U.S. and Japan on finished consumer electronics. Instead,
they focused on the foundation. Through the Industrial Technology
Research Institute (ITRI), the government poured public funds into R&D,
eventually recruiting Morris Chang to commercialize that research. The result
was a consortium-backed model where the state assumed the massive capital
risk of building foundries, allowing the private sector to flourish. This
separated "design" from "manufacturing," creating the fabless revolution.

Israel's NEMO (Neuromorphic Embedded computing architecture for
Mobile applications) consortium mirrors this history, but with a modern,
critical evolution. Backed heavily by the Israel Innovation Authority (IIA) —
the Zionist equivalent of Taiwan's ITRI-NEMO is not just a funding grant; it is
a forced marriage of industry rivals, academic researchers, and defense
contractors. The IIA provides the "risk money," covering a massive percentage
of R&D costs (often up to 66% with no equity taken), effectively de-risking the
"Valley of Death" that killed startups like Mythic.

But here is where the Israeli model diverges from, and arguably improves
upon, the TSMC model.
TSMC's "Pure Play" foundry model is brilliant, but it is fragile. It relies on a
globalized, peaceful supply chain. TSMC needs lithography machines from
the Netherlands (ASML), chemicals from Japan, and designs from California.
If any link in that chain breaks-due to geopolitics, pandemics, or war-the
foundry stops.

Israel, driven by the existential necessity of national security, is building
something tighter: sovereign vertical integration.

The NEMO consortium isn't just building a chip; they are building the "Full
Stack." Because Israel is a "silicon island" geographically isolated by hostile
neighbors, it cannot afford to rely on a fragmented global supply chain for its
critical defense technology.

In this ecosystem, the hardware architects (often veterans of Intel Israel and
Apple's Herzliya silicon teams) sit in the same room as the algorithm
designers from the Technion, who sit next to the product managers from
defense giants like Rafael and Elbit Systems.

This proximity allows for a level of optimization that the distributed TSMC
model cannot match. In the Israeli model, the software stack is written
specifically for the silicon while the silicon is being designed, and the end-
product-whether a loitering munition or a medical vision device-dictates the
specifications of both. This eliminates the "software barrier" that killed Mythic
and the "walled garden" that isolates Intel.

Israel is effectively creating a closed loop of innovation that is immune to
external supply shocks. While Taiwan built the world's factory, Israel is
building the world's brain-and it is ensuring that this brain doesn't need to
ask permission from the rest of the world to function.

To top it all off, all these companies share the same killer app, DDR&D – the
Directorate of Defense Research & Development (often referred to as
MAFAT).

In Silicon Valley, a neuromorphic startup needs to convince a venture
capitalist that there might be a market for their chip in five years. In Israel, the
market exists before the chip does. The Israeli Defense Forces (IDF) have a
critical, immediate need for "edge Al"-drones, loitering munitions, and
communication systems that can process visual and audio data in real-time,
without an internet connection, and on a battery budget of practically zero.

The DDR&D acts as the ultimate anchor tenant. They don't just provide
grants; they provide a guaranteed demand. They effectively say, "If you build
a chip that allows a drone to recognize a target using 1 milliwatt of power, we
will buy it." This removes the market risk that destroyed companies like
Mythic, allowing Israeli startups to focus purely on the technical risk.
And it's working. Israel is the world's leader when it comes to this space, with
companies on every level from product to fab.

Take Tower Semiconductor in Migdal HaEmek. While Intel and TSMC fight a
bloody war over 2nm digital nodes, Tower has quietly cornered the market on
"More than Moore"—the analog technologies that actually interface with the
real world. They are not trying to shrink transistors; they are integrating
sensors directly into the wafer. Their recent $650 million expansion into silicon
photonics and their partnerships with companies like LightIC (for LiDAR) and
Alcyon Photonics show they are building the "eyes and ears" of the machine,
not the brain. They are the only foundry in the world capable of
manufacturing these exotic neuromorphic designs at scale without needing a
new supply chain.

Recently, Tower's stock valuation has skyrocketed-up nearly 190% in the
last year-as Wall Street finally understood that Tower holds the keys to
NVIDIA's kingdom. The massive "interconnect bottleneck" in Al data centers
means that even the fastest Blackwell or Rubin GPUs are limited by how
quickly they can move data between one another. Tower's Silicon Photonics
(SiPho) platform provides the high-speed optical "highways" that allow these
GPUs to communicate at 1.6T and 3.2T speeds, making Tower an essential
partner for the bandwidth requirements of the current Al supercycle. But for
the discerning observer, this bandwidth boom is a Trojan Horse. Investors
believe they are betting on a supporting player in the NVIDIA ecosystem, a
mere plumber for the data center. In reality, they are unwittingly acquiring the
manufacturing backbone of the Al 2.0 revolution. While the market values
Tower today for solving the connectivity problems of the old architecture, its
true explosive potential lies in its monopoly on the exotic processes-like
ReRAM integration and on-chip multi-wavelength lasers-required to build the
new one. They aren't just building the wires for NVIDIA; they are building the
foundry where the first true digital brains will be printed.

Then you have Weebit Nano, which has solved the memory bottleneck. As we
discussed, you cannot have a brain without synapses, and standard Flash
memory is too slow and power-hungry to act as a synapse. Weebit
commercialized ReRAM (Resistive RAM), which behaves almost exactly like
a biological synapse.

Critically, Weebit didn't fall into the "closed garden" trap. Instead of hoarding
the tech, they licensed it to the giants. Just months ago, Weebit secured a
landmark licensing agreement with Texas Instruments. By getting their
ReRAM integrated into Tl's embedded processing chips, they ensured that
Israeli neuromorphic tech will be inside millions of standard industrial devices,
not just niche scientific boards. They effectively forced the industry to adopt
their standard by partnering with the biggest analog chipmaker in history.
Finally, the ecosystem is validated by the massive exits that recycle talent and
capital back into the system. The most striking recent example is Apple's
acquisition of Q.ai.

In January 2026, Apple dropped nearly $2 billion to acquire this relatively
secretive Israeli startup. Q.ai specializes in "silent speech" analysis-using
neuromorphic-style processing to read facial micro-movements and interpret
speech without sound. This wasn't just a software purchase; it was a
hardware play. Apple didn't buy them an app; they bought them to
integrate that "sensing" capability into the next generation of smart glasses
and AirPods.

This acquisition completes the cycle. You have Tower manufacturing the
sensors, Weebit providing the synaptic memory, and startups like Q.ai (and
Hailo for logic) building the end-application. This is a level of full-stack vertical
integration that Silicon Valley cannot match, and it is why the next revolution
in computing isn't happening in Palo Alto.

This revolution is physically mapped onto the land in a way that turns
geography into a competitive advantage. In the north, specifically Migdal
HaEmek, you have the industrial muscle where Tower's fabs physically print
the chips. Move twenty miles west to Haifa, and you hit the "Brain"-home to
the Technion and the deep R&D bunkers of Elbit and Rafael, where the
physics and algorithms are born. Then, you slide down the coast to the Tel
Aviv-Herzliya metro area, the commercial engine where design, software, and
venture capital collide. In the traditional model, the designer is in California
and the manufacturer is in Taiwan. In Israel, the feedback loop between the
academic theory (Haifa), the physical fabrication (Migdal HaEmek), and the
market product (Tel Aviv) is a ninety-minute drive. A flaw discovered in the fab
in the morning is being patched by architects in Haifa by lunch. This
geographic compression effectively transforms an entire country into a single,
cohesive silicon campus.

Al 2.0 and the dotcom bubble
You may have noticed that the term I've been using, “Al 2.0”, sounds a lot like
Web 2.0. This parallel is intentional. If history repeats itself (which it tends to
do), this parallel becomes a warning. Because it is only possible to
understand Web 2.0 in the context of the dotcom bubble which came before it.

I am certainly not the first to draw the analogy between the current state of Al
and the dotcom crash. The analogy is fairly obvious. In the late 1990s,
investors poured billions into companies that promised to revolutionize the
world through the internet, driving the valuations of infrastructure providers
like Cisco into the stratosphere. They weren't wrong about the revolution, but
they were wrong about the timeline and the architecture. They built massive
server farms and laid millions of miles of dark fiber, anticipating a level of
traffic and utility that the dial-up modems and static HTML pages of the era
simply couldn't deliver.

We are currently living through the "Cisco moment" of Al. Just as Cisco
became the most valuable company in the world by selling the routers for the
dotcom boom, NVIDIA has become the titan of the Al boom by selling the
H100s.

Web 1.0 was suffocated by the physical limitations of twisted-pair copper
phone lines. The reason we didn't have YouTube in 1998 wasn't a lack of
video cameras or desire; it was that the infrastructure literally couldn't carry
the signal. We were trying to siphon an ocean through a coffee stirrer. Today's
Al faces an identical crisis, but the bottleneck has moved inside the chassis.
The copper traces connecting a GPU to its memory are the new dial-up
connection. No matter how fast the processor spins, it is left idling, waiting for
data to crawl on the bus, generating heat but no value. Just as the rollout
of broadband and fiber optics around 2004 shattered the bandwidth
constraints of the internet, Al 2.0 requires a similar infrastructure overhaul. By
embedding memory directly into the compute, neuromorphic chips effectively
upgrade the system's internal plumbing from 56k modems to broadband,
unlocking the high-fidelity, real-time capabilities that are currently impossible.

This architectural shift unlocks the functional equivalent of AJAX for the digital
brain. Before the asynchronous web technologies of the mid-2000s, the
internet was a static experience. If you wanted to update a single stock ticker
on a webpage, you had to reload the entire site-header, footer, images, and
all. It was clunky, jarring, and inefficient. Current Al models suffer from this
exact "full page reload" syndrome; learning a single new fact requires re-
running the entire training process, burning gigawatts of energy to update
weights that shouldn't need changing. Neuromorphic computing introduces
the dynamism of Web 2.0 to machine learning. Because it utilizes episodic
memory and synaptic plasticity, the system can update specific local
parameters instantly based on new input without disrupting the global state. It
allows for a "dynamic site" where the Al adapts to the user in real-time,
effectively moving us from the static brochures of GPT-4 to the responsive,
living applications of the future.

Breaking this bottleneck precipitates a shift in power dynamics reminiscent of
the personal computer revolution. We are currently in the mainframe era of Al;
we send our requests to a centralized oracle in a data center and wait for a
response. Al 2.0, driven by efficient, low-power neuromorphic hardware,
brings the "Personal Computer" moment to artificial intelligence. By allowing
complex inference and learning to happen on the edge-on the drone, the
phone, or the headset—we decouple intelligence from the cloud. Thus moving
Al from a service we subscribe to into a tool we physically possess and
control.

We are pouring concrete and burning coal to build data centers the size of
small cities, all to power Large Language Models that are, effectively, the
"Web 1.0" of artificial intelligence. They are static, read-only repositories of
information. They are impressive, yes, but they are tethered to the wall,
expensive to query, and fundamentally incapable of interacting with the
physical world in real-time. The economics work out for select high-margin
domains like code and scientific research, but it cannot work on the edge for
deployments on phones, robots and loT devices.

When the dotcom bubble burst, it wiped out the excess, but it didn't kill the
internet. Instead, it cleared the stage for Web 2.0. The "infrastructure
overhang"-that cheap dark fiber left behind-allowed for the rise of
Facebook, YouTube, and the cloud. It shifted the focus from "how do we get
online" to "what do we do now that we are here?"

The coming correction in Al will be driven by the thermodynamic wall I
mentioned earlier. The market will realize that the current architecture of Al
cannot support the use-cases people actually need. The brute-force era of
"scaling laws"—where we just add more parameters and more power-will hit
a point of diminishing returns.

The irony of the Von Neumann bottleneck is that it was named after a genius
who knew it was a temporary fix. John von Neumann himself was deeply
interested in the workings of the human brain, recognizing that biology had
solved computation problems his architecture could not. For seventy years,
we have been trapped in his temporary fix, optimizing a bottleneck rather than
removing it.

The "Silicon Island" is now removing it. By leveraging a vertically integrated
sovereign ecosystem-from the atomic physics of ReRAM at Weebit, to the
manufacturing lines at Tower, to the defense-hardened algorithms of the IDF
-Israel is forging the hardware that will allow Al to leave the data center and
enter the real world.

The first generation of Al lived in the cloud. Al 2.0 will live in the edge. And the
chips that power it will be born in Israel.
