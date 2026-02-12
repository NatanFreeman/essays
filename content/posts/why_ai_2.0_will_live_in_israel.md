---
title: "The Von Neumann bottleneck: Why AI 2.0 will live in Israel"
date: 2026-02-05T10:00:00-05:00
draft: false
mastodon_post_id: "116058109535082519"
---

## The Philosophical Failure: Breaking the Von Neumann Bottleneck

There has been a sentiment of lament over Israel's supposed failure to invest in
the AI space. "Why isn't there an Israeli ChatGPT?" one might ask. This is
unfair as a lot of the R&D is happening in Israel. Consider
[NVIDIA's significant presence in Israel](https://blogs.timesofisrael.com/nvidias-second-home-why-the-ai-giant-is-doubling-down-on-israel/)
or
[Google DeepMind's Israeli research team](https://research.google/locations/israel/).
Not to mention the work done by universities and startups in this space as well
as the
[Ministry of Defense's dedicated AI unit](https://www.mod.gov.il/English/About/Directorates/Pages/MAFAT.aspx).
One could argue that ChatGPT is the Israeli ChatGPT.

But there is some truth to this sentiment. Israel isn't building data centers to
the same extent as the U.S., and we aren't seeing many foundation models coming
from Israel. But this is not an oversight. Israel is simply looking two steps
ahead. They know they can't directly compete with the U.S. and China in the
current landscape of GPU-dominated large language models. So Israel is building
out the infrastructure for the next generation of AI. The one which will be
defined by lower power costs, greater real-time capabilities and more
decentralization in edge and server environments. Israel is building AI 2.0. The
way they will do that is by breaking the von Neumann bottleneck.

You see there is a glass ceiling to AI which is fundamentally limiting what AI
can do. Whenever we try to incorporate biologically inspired features we hit
this ceiling and fail catastrophically. Attempts to encode episodic memory,
continuous memory, real-time data streaming or efficient processing have either
resulted in low-fidelity implementations or inefficiency with our current
hardware. This is not a failure of implementation; it's a failure of philosophy.
You cannot fix a hardware problem with a software solution.

To understand why a hardware revolution is necessary, we must look at the
specific capabilities that AI 2.0 demands-capabilities that are currently
impossible to implement efficiently.

The first is Episodic Memory, or the ability to learn from a single event
instantly. Consider a child touching a hot stove: they do not need to touch it
ten thousand times to understand it is dangerous. They experience it once, and
their neural pathways physically alter to encode that memory forever. Current AI
cannot do this. To "teach" a neural network a new fact, you must run a massive
training pass, updating billions of parameters in a slow, energy-intensive batch
process. If an autonomous drone flies into a new type of windowpane it hasn't
seen before, it cannot simply "remember" that obstacle for the return trip. It
remains frozen in the state it was trained in until a team of engineers collects
the data, relabels it, and retrains the model in a server farm weeks later. True
autonomy requires the ability to learn continuously from a sample size of one.

This ties directly into the second critical concept: Continuous Learning.
Today's Large Language Models suffer from "catastrophic forgetting." If you try
to teach a pre-trained model a new language or a new medical protocol without
the original training data, it overwrites its previous weights, effectively
forgetting what it used to know. This renders AI systems brittle and static;
they are "frozen brains" trapped in the past. Real-world applications—whether
it's a personalized healthcare assistant tracking a patient's degrading
condition over years, or a missile defense system adapting to a new flight
trajectory mid-air—require a system that can continuously update its
understanding of the world without needing to go offline for a reboot. We need
AI that evolves, not just AI that executes.

Finally, we face the hurdle of Real-Time Data Streaming. We often conflate
"fast" with "real-time," but they are not the same. A GPU is fast because it
processes massive batches of data in parallel, but it has high latency. It waits
to fill a bus with data before crunching the numbers. In contrast, biological
survival depends on processing information as a continuous, noisy stream. A
self-driving car on a highway doesn't have the luxury of batching 50 frames of
video to decide if a pedestrian is stepping out; it needs to process the photon
hitting the sensor immediately. In edge environments, where bandwidth is
nonexistent and decisions must be made in microseconds, the current
"store-then-compute" architecture is simply too slow to survive.

The reason we cannot implement these features today is not a lack of clever
code; it is the von Neumann bottleneck. In our current architecture, the
processing unit (the brain) and the memory unit (the book) are physically
separated, connected by a narrow bus. Every time the AI wants to "think" or
"learn," it must stop, send a request to memory, drag the data across the wire,
compute it, and send the result back.

When we attempt to implement continuous learning or episodic memory, we are
asking the computer to constantly rewrite its own memory. This triggers a
catastrophic traffic jam. The system spends 90% of its time and energy just
moving data back and forth, rather than doing the actual math. This is the
"Memory Wall." It is why training a model takes months and costs millions; we
are paying for the commute, not the calculation. And this isn't just a problem
for battery-constrained drones. In massive data centers, this data movement is
the primary source of heat. We are hitting a thermodynamic wall where scaling up
current AI models is becoming physically impossible because we cannot cool the
wires fast enough to keep up with the data traffic. To build AI 2.0, we must
tear down this wall and build chips where the memory is the computer.

This is what neuromorphic computing has been preaching for over a decade. Yet
companies in this space have failed to reach mass production. But there is one
country looking to break this barrier. In this essay, I will explain exactly
how.

## The Innovator's Dilemma: Why the Giants and Startups Failed

Let us first look at some failures as a test case. Intel's Loihi 3 chip is a key
example.

To be fair, Intel isn't selling vaporware. With the Loihi architecture, they
have successfully demonstrated the immense potential of neuromorphic computing
in tangible, existing applications. They have showcased impressive benchmarks in
adaptive robotics, gesture recognition, and even olfactory sensing, proving that
spiking neural networks can process complex, real-time data with a fraction of
the power budget required by a standard GPU. Technically speaking, the silicon
works.

However, this technical validation is rendered moot by a fatal strategic flaw:
the ecosystem is hermetically sealed. Intel has built a walled garden so high
that it virtually guarantees zero widespread adoption. You cannot simply buy a
Loihi chip off the shelf to integrate into a consumer product, nor can you
easily port existing models to it. Access is largely gatekept behind the
[Intel Neuromorphic Research Community (INRC)](https://www.intel.com/content/www/us/en/research/neuromorphic-community.html),
restricted to cloud-based simulations or strictly vetted academic partnerships.
By forcing developers to use a proprietary, idiosyncratic software stack rather
than integrating seamlessly with open standards, Intel ensures that their
technology remains a niche curiosity rather than an industry standard.

This refusal to open up is not merely an oversight; it is a calculated
hesitation born of the Innovator's Dilemma. Intel is the reigning emperor of the
von Neumann architecture. Their entire trillion-dollar legacy, supply chain, and
revenue stream are built on the x86 instruction set-on high-frequency clock
cycles and the distinct separation of memory and processing. To truly
democratize neuromorphic computing-to make it cheap, accessible, and
interoperable-would be to cannibalize their own core business. Intel cannot
aggressively push a technology that renders their cash cow obsolete. As a
result, they are incentivized to keep neuromorphic computing as an eternal
"science project"-impressive enough to claim innovation, but closed off enough
to ensure it never threatens the dominance of their traditional processors. It
lets them keep a foot in the door without letting anyone else in. Just in case.

This is the Innovator's Dilemma, and we expect it from big companies. But what
about the startups? How are they doing?

Consider Mythic AI, a Texas-based startup that became the poster child for the
dangers of this industry.

Mythic didn't just try to tweak the existing paradigm; they tried to shatter the
von Neumann bottleneck by betting on analog compute-in-memory. Their premise was
brilliant and deeply biologically inspired: instead of shuttling data back and
forth between memory and processors (the exact bottleneck Intel struggles with),
Mythic performed calculations inside the memory arrays themselves using flash
transistors. This mimics the human brain's synapses, where storage and
computation happen in the same place.

On paper, it was revolutionary. They promised the compute power of a desktop GPU
at a fraction of the energy cost, perfect for edge AI. Investors poured in over
$150 million. The industry hype was palpable.

Then, reality hit.

In late 2022,
[Mythic ran out of cash and nearly collapsed](https://mythic.ai/news/mythic-raises-13-5m-in-new-funding-led-by-atw-partners/).
While they have since been "resurrected" by a modest funding round, they serve
as a cautionary tale of a "Zombie Unicorn." Their failure wasn't just financial;
it was a failure to scale a new philosophy in a hardware world built for the old
one.

Mythic faced two insurmountable walls. First, analog computing is incredibly
noisy. Unlike digital logic, which is a clean 0 or 1, analog signals fluctuate
with temperature and manufacturing variances. Trying to tame this "noise"
required complex compensation algorithms that ate away at the very efficiency
gains they promised.

Second, and more fatal, was the software barrier. Just like Intel, Mythic found
that having a brilliant chip is useless if no one can program it. They had to
build their own software stack from scratch because standard tools like PyTorch
and TensorFlow assume digital, deterministic hardware. Developers, already
stretched thin, didn't have the time to learn an entirely new, esoteric coding
language for a chip that might not exist in a year.

Mythic proved that being "better" isn't enough. You can have the most
biologically accurate chip in the world, but if you cannot manufacture it
reliably or integrate it into the existing software supply chain, you are simply
building a very expensive museum piece.

To enter this space, a startup would have to have full vertical integration.
Everything from the market product, to the software stack and even the
lithographic nodes needs to be thought out and developed in a cohesive
ecosystem. This isn't a company – it's an entire industry. And the one place
where this industry is being developed is Israel.

## The Daniel dilemma

Recently, I was discussing this very issue with Dr. Daniel Szenogovski. But we
came to a bit of an impasse. Even if we allow that the future of AI is not in
copper and GPUs, does that mean we should stop all efforts to embed biological
features into our current hardware?

This dilemma is a fundamental tension in the history of technology. Is it worth
investing in cheaper film when digital cameras are on the horizon? Am I wasting
my time making floppier floppy disks when IBM is developing their next
generation of hard drives?

I suppose it depends what your goals are. If you believe we must prove that
biological features "work" using the current hardware, I would be skeptical.
After all, we already have many biological brains in nature. I am not sure we
need a digital model when we already have the brain of say a fly for example,
which is proven to work and consumes only a few microwatts.

If you wish to get some of the benefits of biological models without having to
wait for a hardware shift, it's a matter of timelines. If we have neuromorphic
hardware in a couple years, you might be wasting your time. But if it will take
decades, then you might not want to wait.

But then this decision _itself_ can create a self-fulfilling prophecy. The
longer we work on the current technology, the more we are advancing the _local
maxima_. That is, we improve the technological edge with the architectures we
use today. But as a result, we get stuck. Even if we _would_ eventually achieve
better performance on different hardware, and reach the _global maxima_, we
won't get there until we descend down the slope of our current progress. The
first neuromorphic computers will be worse when going head-to-head with a
traditional LLM running on an RTX 5090. Nobody wants to go backwards.

This stronghold of the GPU is called the "Hardware Lottery". Coined by
researcher Sara Hooker, the Hardware Lottery argues that a research idea (like
Engrams or Neuromorphic computing) wins or loses not because it is inherently
"good" or "bad," but because of its compatibility with available hardware. The
result is that researchers often abandon superior ideas because they don't want
to "lose the lottery" by using hardware that hasn't been optimized for 20 years.

The way we leave this maximization trap is by developing applications which
cannot be done with GPUs. For instance, consider a pair of smart headphones that
must filtering out the roar of a jet engine whilst still allowing human voice to
pass through. Or a wearable cardiac monitor that must learn the unique, shifting
rhythm of a single patient’s heart to detect a one-in-a-million anomaly without
draining its battery by noon. Finally, consider a loitering drone that must
navigate a dense forest in real-time, adapting its flight path to a single
fallen branch it has never seen before. Traditional GPUs fail these tasks
because they are "batch" processors; they require too much power and introduce
too much latency by constantly shuttling data between separate memory and
compute units. These real-world, "always-on" scenarios demand a hardware
architecture where the memory is the computer, allowing for the
microsecond-latency and milliwatt-budget that the physical world—and the human
body—require.

In these applications, it doesn't matter if the newer hardware is "worse" or
will take longer to develop, because it is impossible to achieve them otherwise.

## The Silicon Island: Israel’s Sovereign Vertical Integration

It's natural to draw analogies between Israel's neuromorphic computing industry
and Taiwan's silicon industry from the 1980s. This is by design of course.
Israel has learned the lessons used to transform Taiwan into the world's chip
giant and is applying them to make Israel the home for AI 2.0. Not just for
industry, but as a matter of national security.

To understand the magnitude of what is happening in Israel, we must first
correct a common misconception about the rise of TSMC. Taiwan Semiconductor
Manufacturing Company was not born from the scrappy ambition of a garage
startup; it was a state-engineered miracle.

In the 1970s and 80s, the Taiwanese government realized they could not compete
with the U.S. and Japan on finished consumer electronics. Instead, they focused
on the foundation. Through the Industrial Technology Research Institute (ITRI),
the government poured public funds into R&D, eventually recruiting Morris Chang
to commercialize that research. The result was a consortium-backed model where
the state assumed the massive capital risk of building foundries, allowing the
private sector to flourish. This separated "design" from "manufacturing,"
creating the fabless revolution.

Israel's
[NEMO (Neuromorphic Embedded computing architecture for Mobile applications) consortium](https://amsg.technion.ac.il/nemo-consortium/)
mirrors this history, but with a modern, critical evolution. Backed heavily by
the Israel Innovation Authority (IIA)—the Israeli equivalent of Taiwan's
ITRI—NEMO is not just a funding grant; it is a forced marriage of industry
rivals, academic researchers, and defense contractors. The IIA provides the
"risk money," covering a massive percentage of R&D costs (often up to 66% with
no equity taken), effectively de-risking the "Valley of Death" that killed
startups like Mythic.

But here is where the Israeli model diverges from, and arguably improves upon,
the TSMC model. TSMC's "Pure Play" foundry model is brilliant, but it is
fragile. It relies on a globalized, peaceful supply chain. TSMC needs
lithography machines from the Netherlands (ASML), chemicals from Japan, and
designs from California. If any link in that chain breaks—due to geopolitics,
pandemics, or war—the foundry stops.

Israel, driven by the existential necessity of national security, is building
something tighter: sovereign vertical integration.

The NEMO consortium isn't just building a chip; it is building the "Full Stack."
Because Israel is a "silicon island" geographically isolated by hostile
neighbors, it cannot afford to rely on a fragmented global supply chain for its
critical defense technology.

In this ecosystem, the hardware architects (often veterans of Intel Israel and
Apple's Herzliya silicon teams) sit in the same room as the algorithm designers
from the Technion, who sit next to the product managers from defense giants like
Rafael and Elbit Systems.

This proximity allows for a level of optimization that the distributed TSMC
model cannot match. In the Israeli model, the software stack is written
specifically for the silicon while the silicon is being designed, and the
end-product—whether a loitering munition or a medical vision device—dictates the
specifications of both. This eliminates the "software barrier" that killed
Mythic and the "walled garden" that isolates Intel.

Israel is effectively creating a closed loop of innovation that is immune to
external supply shocks. While Taiwan built the world's factory, Israel is
building the world's brain—and it is ensuring that this brain doesn't need to
ask permission from the rest of the world to function.

To top it all off, all these companies share the same killer app,
[DDR&D—the Directorate of Defense Research & Development (often referred to as MAFAT)](https://www.mod.gov.il/English/About/Directorates/Pages/MAFAT.aspx).

In Silicon Valley, a neuromorphic startup needs to convince a venture capitalist
that there might be a market for their chip in five years. In Israel, the market
exists before the chip does. The Israeli Defense Forces (IDF) have a critical,
immediate need for "edge AI"—drones, loitering munitions, and communication
systems that can process visual and audio data in real-time, without an internet
connection, and on a battery budget of practically zero.

The DDR&D acts as the ultimate anchor tenant. They don't just provide grants;
they provide a guaranteed demand. They effectively say, "If you build a chip
that allows a drone to recognize a target using 1 milliwatt of power, we will
buy it." This removes the market risk that destroyed companies like Mythic,
allowing Israeli startups to focus purely on the technical risk. And it's
working. Israel is the world's leader when it comes to this space, with
companies on every level from product to fab.

Take Tower Semiconductor in Migdal HaEmek. While Intel and TSMC fight a bloody
war over 2nm digital nodes, Tower has quietly cornered the market on "More than
Moore"—the analog technologies that actually interface with the real world. They
are not trying to shrink transistors; they are integrating sensors directly into
the wafer. Their recent
[$650 million expansion into silicon photonics](https://towersemi.com/2024/05/22/tower-semiconductor-announces-major-expansion-of-silicon-photonics-manufacturing-capacity/)
and their partnerships with companies like LightIC (for LiDAR) and Alcyon
Photonics show they are building the "eyes and ears" of the machine, not the
brain. They are the only foundry in the world capable of manufacturing these
exotic neuromorphic designs at scale without needing a new supply chain.

Recently, Tower's stock valuation has skyrocketed—up nearly 190% in the last
year—as Wall Street finally understood that Tower holds the keys to NVIDIA's
kingdom. The massive "interconnect bottleneck" in AI data centers means that
even the fastest Blackwell or Rubin GPUs are limited by how quickly they can
move data between one another. Tower's Silicon Photonics (SiPho) platform
provides the high-speed optical "highways" that allow these GPUs to communicate
at 1.6T and 3.2T speeds, making Tower an essential partner for the bandwidth
requirements of the current AI supercycle. But for the discerning observer, this
bandwidth boom is a Trojan Horse. Investors believe they are betting on a
supporting player in the NVIDIA ecosystem, a mere plumber for the data center.
In reality, they are unwittingly acquiring the manufacturing backbone of the AI
2.0 revolution. While the market values Tower today for solving the connectivity
problems of the old architecture, its true explosive potential lies in its
monopoly on the exotic processes—like ReRAM integration and on-chip
multi-wavelength lasers—required to build the new one. They aren't just building
the wires for NVIDIA; they are building the foundry where the first true digital
brains will be printed.

Then you have Weebit Nano, which has solved the memory bottleneck. As we
discussed, you cannot have a brain without synapses, and standard Flash memory
is too slow and power-hungry to act as a synapse. Weebit commercialized ReRAM
(Resistive RAM), which behaves almost exactly like a biological synapse.

Critically, Weebit didn't fall into the "closed garden" trap. Instead of
hoarding the tech, they licensed it to the giants. Just months ago, Weebit
secured a landmark
[licensing agreement with Texas Instruments](https://www.weebit-nano.com/press-release/weebit-nano-signs-licensing-agreement-with-texas-instruments/).
By getting their ReRAM integrated into TI's embedded processing chips, they
ensured that Israeli neuromorphic tech will be inside millions of standard
industrial devices, not just niche scientific boards. They effectively forced
the industry to adopt their standard by partnering with the biggest analog
chipmaker in history. Finally, the ecosystem is validated by the massive exits
that recycle talent and capital back into the system. The most striking recent
example is Apple's acquisition of Q.ai.

In January 2026, Apple dropped nearly $2 billion to acquire this relatively
secretive
[Israeli startup](https://www.calcalistech.com/ctechnews/article/hkt8lmsat).
Q.ai specializes in "silent speech" analysis-using neuromorphic-style processing
to read facial micro-movements and interpret speech without sound. This wasn't
just a software purchase; it was a hardware play. Apple didn't buy themselves an
app; they bought them to integrate that "sensing" capability into the next
generation of smart glasses and AirPods.

This acquisition completes the cycle. You have Tower manufacturing the sensors,
Weebit providing the synaptic memory, and startups like Q.ai (and Hailo for
logic) building the end-application. This is a level of full-stack vertical
integration that Silicon Valley cannot match, and it is why the next revolution
in computing isn't happening in Palo Alto.

This revolution is physically mapped onto the land in a way that turns geography
into a competitive advantage. In the north, specifically Migdal HaEmek, you have
the industrial muscle where Tower's fabs physically print the chips. Move twenty
miles west to Haifa, and you hit the "Brain"-home to the Technion and the deep
R&D bunkers of Elbit and Rafael, where the physics and algorithms are born.
Then, you slide down the coast to the Tel Aviv-Herzliya metro area, the
commercial engine where design, software, and venture capital collide. In the
traditional model, the designer is in California and the manufacturer is in
Taiwan. In Israel, the feedback loop between the academic theory (Haifa), the
physical fabrication (Migdal HaEmek), and the market product (Tel Aviv) is a
ninety-minute drive. A flaw discovered in the fab in the morning is being
patched by architects in Haifa by lunch. This geographic compression effectively
transforms an entire country into a single, cohesive silicon campus.

## AI 2.0 and the dot-com bubble

You may have noticed that the term I've been using, “AI 2.0”, sounds a lot like
Web 2.0. This parallel is intentional. If history repeats itself (which it tends
to do), this parallel becomes a warning. Because it is only possible to
understand Web 2.0 in the context of the dot-com bubble which came before it.

I am certainly not the first to draw the analogy between the current state of AI
and the dot-com crash. The analogy is fairly obvious. In the late 1990s,
investors poured billions into companies that promised to revolutionize the
world through the internet, driving the valuations of infrastructure providers
like Cisco into the stratosphere. They weren't wrong about the revolution, but
they were wrong about the timeline and the architecture. They built massive
server farms and laid millions of miles of dark fiber, anticipating a level of
traffic and utility that the dial-up modems and static HTML pages of the era
simply couldn't deliver.

We are currently living through the "Cisco moment" of AI. Just as Cisco became
the most valuable company in the world by selling the routers for the dot-com
boom, NVIDIA has become the titan of the AI boom by selling the H100s.

Web 1.0 was suffocated by the physical limitations of twisted-pair copper phone
lines. The reason we didn't have YouTube in 1998 wasn't a lack of video cameras
or desire; it was that the infrastructure literally couldn't carry the signal.
We were trying to siphon an ocean through a coffee stirrer. Today's AI faces an
identical crisis, but the bottleneck has moved inside the chassis. The copper
traces connecting a GPU to its memory are the new dial-up connection. No matter
how fast the processor spins, it is left idling, waiting for data to crawl on
the bus, generating heat but no value. Just as the rollout of broadband and
fiber optics around 2004 shattered the bandwidth constraints of the internet, AI
2.0 requires a similar infrastructure overhaul. By embedding memory directly
into the compute, neuromorphic chips effectively upgrade the system's internal
plumbing from 56k modems to broadband, unlocking the high-fidelity, real-time
capabilities that are currently impossible.

This architectural shift unlocks the functional equivalent of AJAX for the
digital brain. Before the asynchronous web technologies of the mid-2000s, the
internet was a static experience. If you wanted to update a single stock ticker
on a webpage, you had to reload the entire site-header, footer, images, and all.
It was clunky, jarring, and inefficient. Current AI models suffer from this
exact "full page reload" syndrome; learning a single new fact requires re-
running the entire training process, burning gigawatts of energy to update
weights that shouldn't need changing. Neuromorphic computing introduces the
dynamism of Web 2.0 to machine learning. Because it utilizes episodic memory and
synaptic plasticity, the system can update specific local parameters instantly
based on new input without disrupting the global state. It allows for a "dynamic
site" where the AI adapts to the user in real-time, effectively moving us from
the static brochures of GPT-4 to the responsive, living applications of the
future.

We are pouring concrete and burning coal to build data centers the size of small
cities, all to power Large Language Models that are, effectively, the "Web 1.0"
of artificial intelligence. They are static, read-only repositories of
information. They are impressive, yes, but they are tethered to the wall,
expensive to query, and fundamentally incapable of interacting with the physical
world in real-time. The economics work out for select high-margin domains like
code and scientific research, but it cannot work on the edge for deployments on
phones, robots and IoT devices.

When the dot-com bubble burst, it wiped out the excess, but it didn't kill the
internet. Instead, it cleared the stage for Web 2.0. The "infrastructure
overhang"-that cheap dark fiber left behind-allowed for the rise of Facebook,
YouTube, and the cloud. It shifted the focus from "how do we get online" to
"what do we do now that we are here?"

The coming correction in AI will be driven by the thermodynamic wall I mentioned
earlier. The market will realize that the current architecture of AI cannot
support the use-cases people actually need. The brute-force era of "scaling
laws"—where we just add more parameters and more power-will hit a point of
diminishing returns.

The irony of the von Neumann bottleneck is that it was named after a genius who
knew it was a temporary fix. John von Neumann himself was deeply interested in
the workings of the human brain, recognizing that biology had solved computation
problems his architecture could not. For seventy years, we have been trapped in
his temporary fix, optimizing a bottleneck rather than removing it.

The "Silicon Island" is now removing it. By leveraging a vertically integrated
sovereign ecosystem-from the atomic physics of ReRAM at Weebit, to the
manufacturing lines at Tower, to the defense-hardened algorithms of the IDF
-Israel is forging the hardware that will allow AI to leave the data center and
enter the real world.

The first generation of AI lived in the cloud. AI 2.0 will live in the edge. And
the chips that power it will be born in Israel.

## You can throw it out of a window

I talked about Web 2.0, but I'd like to touch on another revolution in
computing. That is, of course, the personal computer revolution.

In the early 1960s, public and cultural perceptions of computers were nothing
like they are today. They were characterized by the image of the "Big Brother"
machine: a centralized, dehumanizing tool of state surveillance and bureaucratic
oppression. This perception was not just a science-fiction trope, but a reaction
to the physical and social reality of how computers existed at the time.

There was no such thing as a "personal" computer. Computers (mainframes) were
massive, room-sized machines owned exclusively by the government, the military,
or giant corporations like IBM.

Only once the personal revolution happened did this view start to shift. A group
of counterculture hackers began to argue that computers didn't have to be "Big
Brother" tools. If individuals could have their own computers, the machines
could become tools for personal liberation and "human augmentation" rather than
oppression.

What I find to be the most telling piece of media from this era is the
[1981 interview with Steve Jobs on ABC news](https://www.youtube.com/watch?v=3H-Y-D3-j-M).
I implore everyone reading this to watch the interview immediately. There are
two things which are particularly striking about it. The first is that both
David Burnham (who warned about the dangers of computers) and Steve Jobs were
right. Computers do compromise people's privacy and are used to oppress people.
But they also enable personal expression and communication on levels that were
never before possible. Equally as interesting is that this interview is not from
1981 - it's from 2031.

Just replace the word "computer" with "AI" and the meaning is the same. Let's
hear how Steve Jobs describes the next generation of AI—AI 2.0, which allows for
decentralization and personal expression.

> Many people see it for the first time and they don't think it's a computer -
> it's about 12 pounds you can throw it out the window if the relationship isn't
> going so well. And I think if you look at the process of the technical
> revolution that we're all in, it's a process of taking very centralized things
> and making them very democratic - if you will, very individualized. Making
> them affordable by individuals for a small collection of tasks

We are currently in the mainframe era of AI; we send our requests to a
centralized oracle in a data center and wait for a response. AI 2.0, driven by
efficient, low-power neuromorphic hardware, brings the "Personal Computer"
moment to artificial intelligence. By allowing complex inference and learning to
happen on the edge—on the drone, the phone, or the headset—we decouple
intelligence from the cloud, moving AI from a service we subscribe to into a
tool we physically possess. One we can even throw out the window if the
relationship isn't going so well.

## Does success kill margins?

You might think AI 2.0 taking off would be a slam-dunk for the Israeli market.
But the reality is slightly more complex. You see it's only recently that Israel
has been targeting the AI 2.0 market. Traditionally, fabs like Tower
Semiconductors weren't targeting neuromorphic AI chips - they were building
analog sensors, in what is called Specialty Fab.

The semiconductor world is divided into two churches: the Commodity Fab and the
Specialty Fab. The Commodity Fab—typified by TSMC, Samsung, and Intel—chases
Moore’s Law. Their goal is to shrink transistors to three nanometers, spending
twenty billion dollars per factory to print billions of identical digital
brains. Their game is scale: making the same chip cheaper and faster than anyone
else. The Specialty Fab—typified by Tower Semiconductor—is the domain of the
vintage artisan. They use older, paid-off machines to tweak the physics of the
silicon itself. They don't make the digital brain; they make the analog senses.
They build the sensors that see, the radios that speak, and the power chips that
manage energy. Their game is customization: making a unique chip that performs a
specific trick perfectly.

For the last decade, this division saved Israel. While Asia fought the brutal
price war of the "Digital Brain," Israel quietly enjoyed high margins in the
"Analog Niche." But AI 2.0 is about to break this truce. The core promise of AI
2.0 is that intelligence moves to the edge—meaning smart sensors will go from
being a niche scientific instrument to being a digital brain found in every
toaster, doorbell, and toy car. This creates a massive identity crisis for the
Israeli model. When a technology scales from one million units in medical
devices to one billion units in consumer IoT, the economics flip. The "Artisan"
model collapses, and the "Scale" model takes over. Israel is currently caught in
a pincer movement between two different types of floods.

The first flood comes from China. This is not hypothetical; it is happening now.
Shut out of the high-end market by U.S. sanctions, China has poured billions
into "Legacy Nodes"—the exact technological backyard of Israeli fabs. Chinese
state-subsidized fabs like SMIC are currently building massive overcapacity in
basic power management and image sensor chips. They are flooding the market with
"good enough" sensors at prices no profit-driven company can match. If the AI
2.0 revolution is built upon the same technology as cheap, generic sensors for
smart fridges, China too will pivot and Israel could not compete. That market is
already gone.

The second flood comes from the other end of the political and logistic
spectrum: Taiwan. Historically, TSMC ignored the "specialty" analog market
because it was too small to move their needle. That has changed. TSMC has
realized that AI needs "Eyes" just as much as "Brains," and they have
aggressively expanded their specialty technology division. Analog has become
just another item in their arsenal. They effectively offer a "Supermarket
Bundle." They can tell a client like NVIDIA, "We are already printing your
digital processor; why don't we just print the power and sensor chips on the
same wafer for a discount?" This is happening now. Imagine the technology
powering the sensor and power circuit also powers the brain. They go from
binding two separate technologies into building a single cohesive package on a
bridge they've already built. A standalone boutique like Tower struggles to
compete with that level of integration efficiency.

Thus far, I've been talking about neuromorphic computers as a commodity - but
this _might_ not apply. Commodities are _fungible_. A ton of steel from China is
the same as a ton of steel from the US. But a neuromorphic sensor and guidance
system for a missile or a heart-rate-temperature sensor is _not fungible_. Even
if the Chinese version is 90% cheaper, the US Department of Defense or a Western
Hospital chain cannot buy it due to security risks.

The market, therefore, bifurcates. Consumer tech, i.e. the toaster and other IoT
devices, will use the cheap Chinese commodity sensors. Israel loses this market.
But critical AI, will use "trusted" Israeli/Western sensors. Critical AI is
defined by the high cost of failure—where "good enough" is a death sentence. It
is the intelligence inside a loitering munition that must make a lethal decision
in a GPS-denied environment, the medical implant regulating a heart rhythm in
real-time, or the autonomous infrastructure controller that cannot risk a
"backdoor" in its silicon. In these domains, the provenance of the chip is as
important as its performance. Israel keeps this market because for the
Department of Defense or a surgical robotics pioneer, a subsidized Chinese chip
isn't a bargain; it’s a liability. Israel keeps this market, but it is smaller.

But if you've been paying attention, you'll see that this is actually perfect
for Israel. Sure, this market might not have the sheer volume of the consumer
world, but it operates on a completely different economic logic: non-fungible
value.

The consumer AI market (toasters, toys, generic smart home devices) is a race to
the bottom. It is a commodity market where Chinese state-subsidized fabs can
dominate because a 5-cent difference in chip price determines the winner. In
this world, success kills margins because high volume invites brutal competition
and price erosion.

Critical AI—defense systems, implantable medical devices, and sovereign
infrastructure—is a "Value" market rather than a "Volume" market. For a missile
guidance system or a robotic surgeon, the cost of the chip is a negligible
fraction of the total system cost, but the cost of its failure is infinite. This
allows Israeli companies to command massive margins that the "Toaster-AI"
companies could never dream of.

It is true that the giants of the East—TSMC and the Chinese state-subsidized
ecosystem—will also eventually reach vertical integration. They too will stitch
sensors to logic. But they will do so for the consumer masses, prioritizing
scale and cost. They will build the brains for the world's refrigerators and
gaming consoles.

Israel’s role is not to compete in this ocean of cheap silicon. Its destiny is
to become the fortress of high-trust computing. As the world bifurcates into
rival geopolitical blocs, the "Western" supply chain will desperately need a
source of advanced AI hardware that is not dependent on the fragile peace of the
South China Sea, nor compromised by the strategic ambitions of Beijing.

By treating the entire country as a single, vertically integrated campus—where
the defense minister, the fab manager, and the algorithm designer operate in
lockstep—Israel offers something money cannot buy: sovereignty. The integration
here is not just technical; it is strategic. Israel is not just moving up the
stack; it is building a parallel stack for the critical infrastructure of the
free world.

The first generation of AI was born in the server farms of Silicon Valley. But
the second generation—the one that will fly our planes, secure our borders, and
monitor our health—requires more than just computation. It requires trust. And
that is why AI 2.0 will live in Israel.
