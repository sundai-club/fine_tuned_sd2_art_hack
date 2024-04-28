import replicate

training = replicate.trainings.create(
    version="stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={
        # "input_images": "https://my-domain/my-input-images.zip",
        "input_images": "https://replicate.delivery/pbxt/KkRcYaQgZ1ycE32YPpQesZ7b9fAsHnGEosLTLZRCMGxUif5b/data.zip",
    },
    destination="dididoo-mk/sdxl_demo_sundai_2"
)
print(training)
