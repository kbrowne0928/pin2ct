


def score_translation(score):

    if score > 0 and score <= 36:
        translation = f'The prediction model analyzes the quality and releventness of your uploaded photo. Your current score is {score}, meaning that the quality of your photo will not generate the high level click through rate you are targeting. Above are a list of better and worse performing images, the recommendation is to upload a photo similar to the better performing group.'
    elif score > 36 and score <= 80:
        translation = f'The prediction model analyzes the quality and releventness of your uploaded photo. Your current score is {score}, meaning that your photo will generate a medium level click through rate. Though your photo meets the minimal standards, if it recommended to refer to the better performing pictures above as reference when uploading your photo.'
    else:
        translation = f'The prediction model analyzes the quality and releventness of your uploaded photo. Your current score is {score}, meaning that your photo will generate a high level click through rate. Our recommendation is to your current photo as the basis for ad generation. Please refer above for a group of even better performing and worse performing images.'

    return translation