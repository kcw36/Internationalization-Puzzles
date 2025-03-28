# Puzzle 2 - Detecting Gravitational Waves

Scientists have built a gravitational wave detector, with detector stations all around the world. Unfortunately, the gravitational waves are extremely faint, and often, what the sensors pick up is just noise. Scientists say that a recording can only be trusted if four or more detector stations around the world are triggered at precisely the same time. Only then can we say with a reasonable degree of certainty that we've detected a gravitational wave1.

In the input list, you find the local times when detectors recorded something, and the time zone of that detector station. Go through the list, and find an instance where four signals were recorded at the same time (at least within the same minute).

Your puzzle input is a complete list of recordings. Find the time that a gravitational wave was recorded in four or more places at the same time. Your final answer must be in the exact same format, but with the time zone offset normalized to '+00:00'. In the example above, the answer corresponding to the four contemporary recordings would be 2019-06-05T12:15:00+00:00

When was a gravitational wave recorded in four or more places, expressed as a timestamp normalized to '+00:00'?