import json
import sys
from datetime import datetime, timezone
import dateutil.parser as parser

def valid_dict(inp_dict):# check whether post is valid JSON dictionaries
    try:
        json.loads(inp_dict)
    except json.decoder.JSONDecodeError:
        return False
    return True

def valid_title(inp_dict):# check whether post have either a title or title_text field
    content=json.loads(inp_dict)
    if ("title" in content) or ("title_text" in content):
        return True
    else:
        return False

def valid_time(inp_dict):# check whether post have a valid date time
    if ("createdAt" in inp_dict):
        try:
            # check whether input date time is valid(parse using ISO format)
            datetime_formats = ("%Y-%m-%dT%H:%M:%S%z")
            datetime.strptime(inp_dict['createdAt'], datetime_formats)
            date = parser.isoparse(inp_dict['createdAt'])
            #Standardize date time to the UTC timezone
            inp_dict["createdAt"]=date.astimezone(timezone.utc).isoformat()
            return inp_dict
        except ValueError:
            return False #invalid date time
    else:
        return inp_dict

def valid_author(inp_dict):# check whether post have a valid author
    if ("author" in inp_dict):
        if(inp_dict["author"]=="null" or inp_dict["author"]=="N/A" or inp_dict["author"]==None or inp_dict["author"]=="" or inp_dict["author"].isspace()):
            return False# Remove the post where the author field is empty, null, or N/A.
        else:
            return inp_dict
    else:
        return inp_dict

def valid_cast_count(inp_dict):# check whether post have a valid total count
    if ("total_count" in inp_dict):
        if (type(inp_dict["total_count"])==str ):
            try:
                #check whether total_count is string containing a cast-able number,
                inp_dict["total_count"]=int(inp_dict["total_count"])
                return inp_dict
            except ValueError:
                return False # total_count cannot cast to int
        elif (type(inp_dict["total_count"])==int or type(inp_dict["total_count"])==float):
            inp_dict["total_count"] = int(inp_dict["total_count"])#total_count is cast to an int
            return inp_dict
        else:
            return False# total_count cannot cast to int
    else:
        return inp_dict

def valid_tag(inp_dict):# check whether post have a valid tags
    if ("tags" in inp_dict):
        i=-1
        for element in inp_dict["tags"]:
            i=i+1
            if(not len(element.split())>1):
                continue
            else:
                temp1 = inp_dict["tags"].pop(i)
                inp_dict["tags"][i:i] = temp1.split()
        return inp_dict
    else:
        return inp_dict

def rekey(inp_dict, keys_replace):# rename title_text field to title.
    return {keys_replace.get(k, k): v for k, v in inp_dict.items()}

def loads_dict(inp_dict):# Loads JSON dictoionary
    return json.loads(inp_dict)

def main():

    with open(sys.argv[2], 'r') as file:
        with open(sys.argv[4], 'w') as file_1:
            for line in file:
                if(valid_dict(line) and valid_title(line)):# if the line is a valid dictoionary with valid title
                    data = json.loads(line)# loads the line
                    if ("title" in data):
                        if (valid_time(data) == False): # remove the line with invalid datetime
                            continue
                        if (valid_author(data) == False):# remove the line with invalid author
                            continue
                        if (valid_cast_count(data)== False):# remove the line with invalid total_count
                            continue
                        data=valid_tag(data)#split the tags
                        json.dump(data, file_1)#write the modified line to output file
                        file_1.write('\n')#add a new line character
                    else:#dictionary with title_text field
                        data = json.loads(line)# loads the line
                        data = rekey(data, {"title_text": "title"})# rename title_text field to title
                        if (valid_time(data) == False):# remove the line with invalid datetime
                            continue
                        if(valid_author(data)==False):# remove the line with invalid author
                            continue
                        if (valid_cast_count(data)== False):# remove the line with invalid total_count
                            continue
                        data = valid_tag(data)#split the tags
                        json.dump(data, file_1)#write the modified line to output file
                        file_1.write('\n')#add a new line character
                else:
                    continue

if __name__ == '__main__':
    main()
