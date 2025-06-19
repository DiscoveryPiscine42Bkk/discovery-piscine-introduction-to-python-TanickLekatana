farm_tasks = []

def display_menu():
    print("\n===== Smart Farm TUG TUG TUG =====")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภทงาน: ")
    farm_tasks.append({"name": name, "category": category})
    print("✅ เพิ่มงานเรียบร้อยแล้ว")

def show_tasks():
    if not farm_tasks:
        print("ไม่มีงานในระบบ")
        return
    print("\n📋 รายการงานทั้งหมด:")
    for i, task in enumerate(farm_tasks, start=1):
        print(f"{i}. {task['name']} ({task['category']})")

def delete_task():
    show_tasks()
    if not farm_tasks:
        return
    try:
        index = int(input("กรุณาระบุหมายเลขงานที่ต้องการลบ: "))
        if 1 <= index <= len(farm_tasks):
            removed = farm_tasks.pop(index - 1)
            print(f"🗑️ ลบงาน '{removed['name']}' เรียบร้อยแล้ว")
        else:
            print("❌ หมายเลขไม่ถูกต้อง")
    except ValueError:
        print("❌ กรุณาใส่ตัวเลขเท่านั้น")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task['category']
        summary[category] = summary.get(category, 0) + 1

    print("\n📊 สรุปจำนวนงานในแต่ละประเภท:")
    if not summary:
        print("ไม่มีข้อมูล")
    else:
        for cat, count in summary.items():
            print(f"- {cat}: {count} งาน")

def main():
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            summarize_tasks()
        elif choice == '5':
            print("👋 ออกจากโปรแกรมแล้ว")
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main()