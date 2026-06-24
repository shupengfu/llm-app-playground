def build_prompt(task_type: str, user_input: str) -> str:
    if task_type == "summary":
        return f"""
你是一个专业的文本总结助手。

请总结下面的内容，要求：
1. 保留核心信息
2. 语言简洁清晰
3. 不要添加原文没有的信息
4. 输出分点总结

原文：
{user_input}
"""

    if task_type == "code_explain":
        return f"""
你是一个专业的编程教学助手。

请详细解释下面这段代码，要求：
1. 先说明代码整体作用
2. 再分模块解释关键代码
3. 说明关键变量和函数的作用
4. 最后总结这段代码适合用在什么场景

代码：
{user_input}
"""

    if task_type == "daily_report":
        return f"""
你是一个专业的工作日报整理助手。

请根据下面的工作内容，整理成一份清晰的工作日报，要求：
1. 今日主要工作
2. 具体完成内容
3. 遇到的问题和解决方式
4. 下一步计划
5. 语气正式，适合发给导师或领导

工作内容：
{user_input}
"""

    if task_type == "polish_translate":
        return f"""
你是一个专业的中英文写作润色助手。

请对下面的内容进行翻译或润色，要求：
1. 如果是中文，请润色成更自然、正式的中文
2. 如果是英文，请润色成更自然、专业的英文
3. 保留原意
4. 不要随意增加事实

内容：
{user_input}
"""

    return f"""
请根据用户输入完成任务。

用户输入：
{user_input}
"""