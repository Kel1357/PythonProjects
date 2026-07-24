import pickle
import matplotlib.pyplot as plt
from datetime import datetime
class Resume:
    def __init__(self):
        pass
    def load_records(self):
        try:
            with open("resume.data", "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError,EOFError):
            return []
        except Exception:
            return []
    def save_all_records(self,records):
        try:
            with open("resume.data", "wb") as f:
                pickle.dump(records, f)
            print("Data Saved Successfully")
        except Exception:
            print("Data Not Saved")
    def next(self,records):
        if not records:
            return 1
        h=records[0]["id"]
        for rec in records:
            if rec["id"]>h:
                h=rec["id"]
        return h+1
    def input(self,prompt):
        print(prompt+ "(type 'end' on a new line to finish)")
        result=""
        f=True
        while True:
            l=input()
            if l.strip().lower()=="end":
                break
            if f:
                result=l
                f=False
            else:
                result=result+"\n"+l
        return result
    def save_data(self):
        records=self.load_records()
        try:
            print("\n---Header---")
            fn=input("Full Name:")
            ph=input("Phone Number:")
            email=input("Email Address:")
            linkedin=input("LinkedIn URL:")
            port=input("Portfolio / GitHub URL:")
            city=input("Location (City, State):")

            print("\n---Professional Summary---")
            summary=self.input("Summary Of Your Experience & Strengths:")

            print("\n---Education---")
            education=self.input("Degree, University, Years, Location, Coursework, CGPA, etc.:")

            print("\n---Experience---")
            experience=self.input("Job Title, Company, Years, Location and Bullet Points of what you did:")

            print("\n---Projects---")
            projects=self.input("Project Name, Technologies Used, Years and What the Project Does:")

            print("\n---Technical Skills---")
            skills=self.input("Languages/Frameworks/Tools, Eg:'Languages: Python, Java, SQL, etc':")

            print("\n---Certifications---")
            cert=self.input("Certification Name - Issuing Organization - Date:")

            print("\n---Leaderships/Activities---")
            leader=self.input("Organisation / Role, Years, Location and Impact:")

            records.append({
                "id": self.next(records),
                "Full Name": fn,
                "Phone Number": ph,
                "Email Address": email,
                "LinkedIn URL": linkedin,
                "Portfolio / GitHub URL": port,
                "City, State": city,
                "Summary": summary,
                "Education": education,
                "Experience": experience,
                "Projects": projects,
                "Skills": skills,
                "Certifications": cert,
                "Leaderships": leader,
                "Created On": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })
            self.save_all_records(records)
        except ValueError:
            print("Invalid Data, Please Try Again")
    def show_data(self):
        records=self.load_records()
        if not records:
            print("No Records Found")
            return
        print("\nID\tName\t\t\t\tEmail\t\t\t\t\tPhone")
        for rec in records:
            print(f"{rec['id']}\t{rec['Full Name']:<20}{rec['Email Address']:<20}\t{rec['Phone Number']:<11}")
    def sort_data(self,p=True):
        self.show_data()
        records = self.load_records()
        print("\nCreated On:")
        for rec in records:
            print(rec["id"],rec["Created On"])
        if not records:
            print("No Records Found")
            return
        if p:
            print("\nSort: 1-Name/2-Date Created")
            ch = input("Sorting Choice:").strip()
            key = {"1": "Full Name", "2": "Created On"}
            k = key.get(ch)
            if not k:
                print("Invalid Choice, Please Try Again")
                return
            order = input("Order: 1-Ascending/2-Descending:").strip()
            reverse=(order == "2")
            n=len(records)
            for i in range(n):
                for j in range(n-i-1):
                    a=records[j][k]
                    b=records[j+1][k]
                    if k == "Created On":
                        a = datetime.strptime(a, "%Y-%m-%d %H:%M")
                        b = datetime.strptime(b, "%Y-%m-%d %H:%M")
                    else:
                        a = a.lower()
                        b = b.lower()
                    if (a>b and not reverse) or (a<b and reverse):
                        t=records[j]
                        records[j]=records[j+1]
                        records[j+1]=t
            for i, r in enumerate(records, start=1):
                r["id"] = i
            self.save_all_records(records)
    def find(self, records, rid):
        for r in records:
            if r['id'] == rid:
                return r
        return None
    def print(self, r):
        print("\n" + "=" * 60)
        print(f"{r['Full Name']:^60}")
        print(f"{r['City, State']} | {r['Phone Number']} | {r['Email Address']}".center(60))
        print(f"{r['LinkedIn URL']} | {r['Portfolio / GitHub URL']}".center(60))
        print("=" * 60)

        print("\nPROFESSIONAL SUMMARY")
        print("-" * 60)
        print(f"{r['Summary']}")

        print("\nEDUCATION")
        print("-" * 60)
        print(r['Education'])

        print("\nEXPERIENCE")
        print("-" * 60)
        print(r['Experience'])

        print("\nPROJECTS")
        print("-" * 60)
        print(r['Projects'])

        print("\n TECHNICAL SKILLS")
        print("-" * 60)
        print(r['Skills'])

        print("\nCERTIFICATIONS")
        print("-" * 60)
        print(r['Certifications'])

        print("\nLEADERSHIP/ACTIVITIES")
        print("-" * 60)
        print(r['Leaderships'])

        print("\n" + "=" * 60)
        print(f"Created On: {r['Created On']}")
        print("=" * 60)
    def view_data(self):
        self.show_data()
        try:
            rid=int(input("Enter Resume ID To View:"))
        except ValueError:
            print("Invalid Value, Please Try Again")
            return
        records=self.load_records()
        r=self.find(records, rid)
        if not r:
            print("Resume Not Found")
            return
        self.print(r)
    def update_data(self):
        self.show_data()
        try:
            rid=int(input("Enter Resume ID To Update:"))
        except ValueError:
            print("Invalid Value, Please Try Again")
            return
        records=self.load_records()
        r=self.find(records,rid)
        if not r:
            print("Resume Not Found")
            return
        field={
            "1": ("Full Name", "Full Name", False),
            "2": ("Phone Number", "Phone Number", False),
            "3": ("Email Address", "Email Address", False),
            "4": ("LinkedIn URL", "LinkedIn URL", False),
            "5": ("Portfolio / GitHub URL", "Portfolio / GitHub URL", False),
            "6": ("Location (City, State)", "Location (City, State)", False),
            "7": ("Summary", "Summary", False),
            "8": ("Education", "Education", False),
            "9": ("Experience", "Experience", False),
            "10": ("Projects", "Projects", False),
            "11": ("Skills", "Skills", False),
            "12": ("Certifications", "Certifications", False),
            "13": ("Leaderships", "Leaderships / Activities", False),
        }
        while True:
            print("\nWhich Field, Do you want To Update?")
            for k,v in field.items():
                print(f"{k}. {v[1]}")
            print("0. Done Updating")
            choice=input("Enter Your Choice:")
            if choice=="0":
                break
            if choice not in field:
                print("Invalid Choice, Please Try Again")
                continue
            fields, label, m = field[choice]
            if m:
                r[fields]=self.input(f"Enter New {label}:")
            else:
                r[fields]=input(f"Enter New {label}:")
            self.save_all_records(records)
            print(f"{label} Updated")
            a=input("Do you want to Update Another Field? 1-Yes/0-No:")
            if a!="1":
                break
    def backup_data(self):
        try:
            with open("resume.data","rb") as s:
                c=s.read()
            t=datetime.now().strftime("%Y-%m-%d_%H-%M")
            backup=f"resume_backup_{t}.data"
            with open(backup,"wb") as b:
                b.write(c)
            print(f"Backup Created: {backup}")
        except FileNotFoundError:
            print("No File Exists To Backup")
        except Exception:
            print("Backup Creation Failed")
    def delete_data(self):
        self.show_data()
        rid=input("Enter Resume Id To Delete (Separated By Commas):").strip()
        try:
            choice=[]
            for c in rid.split(","):
                choice.append(int(c))
        except ValueError:
            print("Invalid Value, Please Try Again")
            return
        records=self.load_records()
        e=[r["id"] for r in records]
        v=[c for c in choice if c in e]
        if not v:
            print("Resume Not Found")
            return
        c=input(f"Delete Resume Id(s) {v}? 1-Yes/0-No:")
        if c!="1":
            print("Cancelled Resume Deletion")
            return
        new=[]
        for x in records:
            if x['id'] not in v:
                new.append(x)
        records=new
        self.save_all_records(records)
        print("Data Deleted Successfully")
    def restore_data(self):
        backup=input("Enter the Backup Filename To Restore:").strip()
        try:
            with open(backup,"rb") as f:
                old=pickle.load(f)
        except FileNotFoundError:
            print("No Backup File Exists To Restore")
            return
        except Exception:
            print("Restoration Failed")
            return
        current=self.load_records()
        on={r["Full Name"]: r for r in old}
        cn= [r["Full Name"] for r in current]
        m=[]
        for name,r in on.items():
            if name not in cn:
                m.append(r)
        if not m:
            print("No Deleted Resume Found in the Backup")
            return
        print("\nDeleted Resume Found:")
        for i,r in enumerate(m,start=1):
            print(f"{i}. {r['Full Name']}")
        num=input("Enter the number To Restore (Separated By Commas):").strip()
        try:
            choice=[]
            for c in num.split(","):
                choice.append(int(c))
        except ValueError:
            print("Invalid Value, Please Try Again")
            return
        k=len(m)
        rn=[]
        for ch in choice:
            if ch<1 or ch>k:
                print(f"Invalid Choice: {ch}")
                continue
            restored=m[ch-1]
            restored["id"]=self.next(current)
            current.append(restored)
            rn.append(restored["Full Name"])
        self.save_all_records(current)
        res=""
        for i,name in enumerate(rn):
            if i==0:
                res=name
            else:
                res=res+","+name
        print(f"Restored: {res}")
    def search_data(self):
        k=input("Enter Any Part Of Name or Skill Keyword:").lower()
        records=self.load_records()
        mat=[]
        for r in records:
            if k in r["Full Name"].lower() or k in r["Skills"].lower():
                mat.append(r)
        if not mat:
            print("Resume Not Found")
            return
        print("\nID\tFull Name\t\t\tEmail Address\t\t\tPhone Number\tSkills")
        for r in mat:
            print(f"{r['id']}\t{r['Full Name']:<20}{r['Email Address']:<20}\t{r['Phone Number']:<11}\t\t{r['Skills']}")
    def export_data(self):
        self.show_data()
        try:
            rid=int(input("Enter Resume ID To Export:"))
        except ValueError:
            print("Invalid Value, Please Try Again")
            return
        records=self.load_records()
        r=self.find(records, rid)
        if not r:
            print("Resume Not Found")
            return
        filename=f"{r['Full Name'].replace(' ','')}_resume.txt"
        with open(filename, "w") as f:
            f.write(f"{r['Full Name']:^60}\n")
            f.write(f"{r['City, State']} | {r['Phone Number']} | {r['Email Address']}\n".center(60))
            f.write(f"{r['LinkedIn URL']} | {r['Portfolio / GitHub URL']}\n".center(60))
            f.write("=" * 60 + "\n")

            f.write("\nPROFESSIONAL SUMMARY\n")
            f.write("-" * 60 + "\n")
            f.write(r["Summary"] + "\n")

            f.write("\nEDUCATION\n")
            f.write("-" * 60 + "\n")
            f.write(r["Education"] + "\n")

            f.write("\nEXPERIENCE\n")
            f.write("-" * 60 + "\n")
            f.write(r["Experience"] + "\n")

            f.write("\nPROJECTS\n")
            f.write("-" * 60 + "\n")
            f.write(r["Projects"] + "\n")

            f.write("\nTECHNICAL SKILLS\n")
            f.write("-" * 60 + "\n")
            f.write(r["Skills"] + "\n")

            f.write("\nCERTIFICATIONS\n")
            f.write("-" * 60 + "\n")
            f.write(r["Certifications"] + "\n")

            f.write("\nLEADERSHIPS/ACTIVITIES\n")
            f.write("-" * 60 + "\n")
            f.write(r["Leaderships"] + "\n")
        print(f"Resume Exported to {filename}")
    def clone_data(self):
        self.show_data()
        try:
            rid=int(input("Enter Resume ID To Clone Data From:"))
        except ValueError:
            print("Invalid Value, Please Try Again")
            return
        records=self.load_records()
        r=self.find(records, rid)
        if not r:
            print("Resume Not Found")
            return
        clone=r.copy()
        clone["id"] = self.next(records)
        clone["Full Name"] = r["Full Name"] + " (Copy)"
        clone["Created On"] = datetime.now().strftime("%d/%m/%Y %H:%M")
        base=r["Full Name"]
        exist=[rec["Full Name"] for rec in records]
        count=0
        pre = base + " (Copy"
        for name in exist:
            if name==base + " (Copy)" or name[:len(pre)]==pre:
                count=count+1
        if count==0:
            clone["Full Name"] = base + " (Copy)"
        else:
            clone["Full Name"] =  base + f" (Copy {count + 1})"
        records.append(clone)
        print(f"Cloned: {clone['Full Name']}")
        edit=input("Do You want to Edit this Cloned Resume? 1-Yes/0-No:")
        if edit=="1":
            self.save_all_records([clone])
            self.update_data()
            edited=self.load_records()[0]
            records[-1]=edited
            self.save_all_records(records)
            print(f"Clone Is Updated: {edited['Full Name']}")
        else:
            self.save_all_records(records)
            print(f"Cloned: {clone['Full Name']} Saved Without Editing")
    def stats_data(self):
        records=self.load_records()
        if not records:
            print("Resume Not Found")
            return
        print(f"Total Resumes: {len(records)}")
        c={}
        for r in records:
            raw=(
                r["Skills"]
                .replace("&",",")
                .replace("/",",")
                .replace(" and ",",")
            )
            skills=raw.split(",")
            for s in skills:
                s=s.strip()
                if s=="":
                    continue
                if s in c:
                    c[s]=c[s]+1
                else:
                    c[s]=1
        if not c:
            print("No Skills Available To Plot")
            return
        skill=[]
        count=[]
        for sk in c:
            skill.append(sk)
            count.append(c[sk])
        maxi=0
        for cnt in count:
            if cnt>maxi:
                maxi=cnt
        col=[]
        for cnt in count:
            if cnt==maxi:
                col.append("red")
            else:
                col.append("skyblue")
        plt.figure()
        bars=plt.bar(
            skill, count, color=col, align="center", label="Skills", edgecolor="black", width=0.5
        )
        for bar in bars:
            h=bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                h+0.05,
                f"{int(h)}",
                ha="center",
                va="bottom",
                fontweight="bold",
            )
        plt.title(
            "Candidate Skills (Most Popular Highlighted)",
            fontsize=12,
            pad=15,
        )
        plt.xlabel("Skills Learned By Candidates", fontsize=11)
        plt.ylabel("Number of Candidates", fontsize=11)
        plt.grid(axis="y",linestyle="--",alpha=0.3)
        plt.tight_layout()
        plt.show()
if __name__ == "__main__":
    self=Resume()
    while True:
        print("\nResume Management:")
        print("1. Save The Resume")
        print("2. Show The Resume")
        print("3. Sort The Resume")
        print("4. View The Resume")
        print("5. Update The Resume")
        print("6. Backup The Resume")
        print("7. Delete The Resume")
        print("8. Restore The Resume")
        print("9. Search The Resume")
        print("10. Export The Resume")
        print("11. Clone The Resume")
        print("12. Statistics Of Skills ")
        print("0. Exit")
        try:
            n=int(input("Enter Your Choice:"))
            if n==1:
                self.save_data()
            elif n==2:
                self.show_data()
            elif n==3:
                self.sort_data()
            elif n==4:
                self.view_data()
            elif n==5:
                self.update_data()
            elif n==6:
                self.backup_data()
            elif n==7:
                self.delete_data()
            elif n==8:
                self.restore_data()
            elif n==9:
                self.search_data()
            elif n==10:
                self.export_data()
            elif n==11:
                self.clone_data()
            elif n==12:
                self.stats_data()
            elif n==0:
                print("Program Exited Successfully")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Value, Please Try Again")