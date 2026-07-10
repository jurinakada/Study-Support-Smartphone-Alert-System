#finalizing the final report


def time_convert(seconds):
    #convert seconds to
    #hours, minutes, seconds

    #convert decimal seconds to integer
    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def evaluate_light(brightness):
    #if brightness data does not exist
    if brightness is None:
        return "No brightness data"
    
    #evaluate the brightness
    if brightness >= 0.5:
        return "Bright"
    
    else:
        return "Dark"


def create_final_report(
    study,
    brightness=None,
    temperature=None,
    humidity=None
):
    
    #study time
    study_time = study.get_total_study_time()

    #away time
    away_time = study.get_total_away_time()

    #study time(exclude the away time)
    actual_study_time = study.get_actual_study_time()

    #smartphone usage time
    phone_usage_time = study.get_total_phone_usage_time()

    #warning count
    warning_count = study.warning_count

    #study environment evaluation
    #light evaluation
    light_evaluation = evaluate_light(brightness)

    #create the final report
    final_report = (
        "Final Study Report\n"
        f"Study time: {time_convert(study_time)}\n"
        f"Away time: {time_convert(away_time)}\n"
        f"Actual study time: {time_convert(actual_study_time)}\n"
        f"Phone usage time: {time_convert(phone_usage_time)}\n"
        f"Warning count: {warning_count}\n"
        f"Brightness: {brightness if brightness is not None else 'No data'}\n"
        f"Light evaluation: {light_evaluation}\n"
        f"Temperature: {temperature if temperature is not None else 'No data'}\n"
        f"Humidity: {humidity if humidity is not None else 'No data'}"
    )

    return final_report



