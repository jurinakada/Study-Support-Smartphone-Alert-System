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


def create_report_list(
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

    #light evaluation
    light_evaluation = evaluate_light(brightness)

    #create the report list for Google Spreadsheet
    report_list = [
        time_convert(study_time),
        time_convert(away_time),
        time_convert(actual_study_time),
        time_convert(phone_usage_time),
        warning_count,
        brightness if brightness is not None else "No data",
        light_evaluation,
        temperature if temperature is not None else "No data",
        humidity if humidity is not None else "No data"
    ]

    return report_list