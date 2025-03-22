import os

# 新旧字符串配对列表
replace_pairs = [

(' A_1', ' CB1_CA1'),
(' A_2', ' CB1_CA2'),
(' A_3', ' CB1_CA3'),
(' A_4', ' CB1_CA4'),
(' A_5', ' CB1_CA5'),
(' A_6', ' CB1_CA6'),
(' A_7', ' CB1_CA7'),
(' A_8', ' CB1_CA8'),
(' A_9', ' CB1_CA9'),
(' A_10', ' CB1_CA10'),
(' A_11', ' CB1_CA11'),
(' A_12', ' CB1_CA12'),
(' A_13', ' CB1_CA13'),
(' A_14', ' CB1_CA14'),
(' A_15', ' CB1_CA15'),
(' A_16', ' CB1_CA16'),
(' B_1', ' CB2_CA1'),
(' B_2', ' CB2_CA2'),
(' B_3', ' CB2_CA3'),
(' B_4', ' CB2_CA4'),
(' B_5', ' CB2_CA5'),
(' B_6', ' CB2_CA6'),
(' B_7', ' CB2_CA7'),
(' B_8', ' CB2_CA8'),
(' B_9', ' CB2_CA9'),
(' B_10', ' CB2_CA10'),
(' B_11', ' CB2_CA11'),
(' B_12', ' CB2_CA12'),
(' B_13', ' CB2_CA13'),
(' B_14', ' CB2_CA14'),
(' B_15', ' CB2_CA15'),
(' B_16', ' CB2_CA16'),
(' C_1', ' CB3_CA1'),
(' C_2', ' CB3_CA2'),
(' C_3', ' CB3_CA3'),
(' C_4', ' CB3_CA4'),
(' C_5', ' CB3_CA5'),
(' C_6', ' CB3_CA6'),
(' C_7', ' CB3_CA7'),
(' C_8', ' CB3_CA8'),
(' C_9', ' CB3_CA9'),
(' C_10', ' CB3_CA10'),
(' C_11', ' CB3_CA11'),
(' C_12', ' CB3_CA12'),
(' C_13', ' CB3_CA13'),
(' C_14', ' CB3_CA14'),
(' C_15', ' CB3_CA15'),
(' C_16', ' CB3_CA16'),
(' D_1', ' CB4_CA1'),
(' D_2', ' CB4_CA2'),
(' D_3', ' CB4_CA3'),
(' D_4', ' CB4_CA4'),
(' D_5', ' CB4_CA5'),
(' D_6', ' CB4_CA6'),
(' D_7', ' CB4_CA7'),
(' D_8', ' CB4_CA8'),
(' D_9', ' CB4_CA9'),
(' D_10', ' CB4_CA10'),
(' D_11', ' CB4_CA11'),
(' D_12', ' CB4_CA12'),
(' D_13', ' CB4_CA13'),
(' D_14', ' CB4_CA14'),
(' D_15', ' CB4_CA15'),
(' D_16', ' CB4_CA16'),
(' E_1', ' CB5_CA1'),
(' E_2', ' CB5_CA2'),
(' E_3', ' CB5_CA3'),
(' E_4', ' CB5_CA4'),
(' E_5', ' CB5_CA5'),
(' E_6', ' CB5_CA6'),
(' E_7', ' CB5_CA7'),
(' E_8', ' CB5_CA8'),
(' E_9', ' CB5_CA9'),
(' E_10', ' CB5_CA10'),
(' E_11', ' CB5_CA11'),
(' E_12', ' CB5_CA12'),
(' E_13', ' CB5_CA13'),
(' E_14', ' CB5_CA14'),
(' E_15', ' CB5_CA15'),
(' E_16', ' CB5_CA16'),
(' F_1', ' CB6_CA1'),
(' F_2', ' CB6_CA2'),
(' F_3', ' CB6_CA3'),
(' F_4', ' CB6_CA4'),
(' F_5', ' CB6_CA5'),
(' F_6', ' CB6_CA6'),
(' F_7', ' CB6_CA7'),
(' F_8', ' CB6_CA8'),
(' F_9', ' CB6_CA9'),
(' F_10', ' CB6_CA10'),
(' F_11', ' CB6_CA11'),
(' F_12', ' CB6_CA12'),
(' F_13', ' CB6_CA13'),
(' F_14', ' CB6_CA14'),
(' F_15', ' CB6_CA15'),
(' F_16', ' CB6_CA16'),
(' G_1', ' CB7_CA1'),
(' G_2', ' CB7_CA2'),
(' G_3', ' CB7_CA3'),
(' G_4', ' CB7_CA4'),
(' G_5', ' CB7_CA5'),
(' G_6', ' CB7_CA6'),
(' G_7', ' CB7_CA7'),
(' G_8', ' CB7_CA8'),
(' G_9', ' CB7_CA9'),
(' G_10', ' CB7_CA10'),
(' G_11', ' CB7_CA11'),
(' G_12', ' CB7_CA12'),
(' G_13', ' CB7_CA13'),
(' G_14', ' CB7_CA14'),
(' G_15', ' CB7_CA15'),
(' G_16', ' CB7_CA16'),
(' H_1', ' CB8_CA1'),
(' H_2', ' CB8_CA2'),
(' H_3', ' CB8_CA3'),
(' H_4', ' CB8_CA4'),
(' H_5', ' CB8_CA5'),
(' H_6', ' CB8_CA6'),
(' H_7', ' CB8_CA7'),
(' H_8', ' CB8_CA8'),
(' H_9', ' CB8_CA9'),
(' H_10', ' CB8_CA10'),
(' H_11', ' CB8_CA11'),
(' H_12', ' CB8_CA12'),
(' H_13', ' CB8_CA13'),
(' H_14', ' CB8_CA14'),
(' H_15', ' CB8_CA15'),
(' H_16', ' CB8_CA16'),
(' I_1', ' CB9_CA1'),
(' I_2', ' CB9_CA2'),
(' I_3', ' CB9_CA3'),
(' I_4', ' CB9_CA4'),
(' I_5', ' CB9_CA5'),
(' I_6', ' CB9_CA6'),
(' I_7', ' CB9_CA7'),
(' I_8', ' CB9_CA8'),
(' I_9', ' CB9_CA9'),
(' I_10', ' CB9_CA10'),
(' I_11', ' CB9_CA11'),
(' I_12', ' CB9_CA12'),
(' I_13', ' CB9_CA13'),
(' I_14', ' CB9_CA14'),
(' I_15', ' CB9_CA15'),
(' I_16', ' CB9_CA16'),
(' J_1', ' CB10_CA1'),
(' J_2', ' CB10_CA2'),
(' J_3', ' CB10_CA3'),
(' J_4', ' CB10_CA4'),
(' J_5', ' CB10_CA5'),
(' J_6', ' CB10_CA6'),
(' J_7', ' CB10_CA7'),
(' J_8', ' CB10_CA8'),
(' J_9', ' CB10_CA9'),
(' J_10', ' CB10_CA10'),
(' J_11', ' CB10_CA11'),
(' J_12', ' CB10_CA12'),
(' J_13', ' CB10_CA13'),
(' J_14', ' CB10_CA14'),
(' J_15', ' CB10_CA15'),
(' J_16', ' CB10_CA16'),
(' K_1', ' CB11_CA1'),
(' K_2', ' CB11_CA2'),
(' K_3', ' CB11_CA3'),
(' K_4', ' CB11_CA4'),
(' K_5', ' CB11_CA5'),
(' K_6', ' CB11_CA6'),
(' K_7', ' CB11_CA7'),
(' K_8', ' CB11_CA8'),
(' K_9', ' CB11_CA9'),
(' K_10', ' CB11_CA10'),
(' K_11', ' CB11_CA11'),
(' K_12', ' CB11_CA12'),
(' K_13', ' CB11_CA13'),
(' K_14', ' CB11_CA14'),
(' K_15', ' CB11_CA15'),
(' K_16', ' CB11_CA16'),
(' L_1', ' CB12_CA1'),
(' L_2', ' CB12_CA2'),
(' L_3', ' CB12_CA3'),
(' L_4', ' CB12_CA4'),
(' L_5', ' CB12_CA5'),
(' L_6', ' CB12_CA6'),
(' L_7', ' CB12_CA7'),
(' L_8', ' CB12_CA8'),
(' L_9', ' CB12_CA9'),
(' L_10', ' CB12_CA10'),
(' L_11', ' CB12_CA11'),
(' L_12', ' CB12_CA12'),
(' L_13', ' CB12_CA13'),
(' L_14', ' CB12_CA14'),
(' L_15', ' CB12_CA15'),
(' L_16', ' CB12_CA16'),
('setPinOutput(', 'gpio_set_pin_output_push_pull('),
('setPinInputHigh(', 'gpio_set_pin_input_high('),
('setPinInput(', 'gpio_set_pin_input('),
('readPin(', 'gpio_read_pin('),
('writePin(', 'gpio_write_pin('),
('writePinHigh(', 'gpio_write_pin_high('),
('writePinLow(', 'gpio_write_pin_low('),
('RGB_DISABLE_WHEN_USB_SUSPENDED', 'RGB_MATRIX_SLEEP'),
('LED_DISABLE_WHEN_USB_SUSPENDED', 'LED_MATRIX_SLEEP'),
('ENCODERS_PAD_A', 'ENCODER_A_PINS'),
('ENCODERS_PAD_B', 'ENCODER_B_PINS'),
('BLUETOOTH_INT_OUTPUT_PIN', 'LKBT51_INT_OUTPUT_PIN'),
('P24G_MODE_SELECT_PIN', 'P24G_MODE_SELECT_PIN'),
('LED_DRIVER_SHUTDOWN_PIN', 'SNLED27351_SDB_PIN'),
('MSKPHASE_12CHANNEL', 'SNLED27351_SCAN_PHASE_12_CHANNEL'),
('MSKPHASE_11CHANNEL', 'SNLED27351_SCAN_PHASE_11_CHANNEL'),
('MSKPHASE_10CHANNEL', 'SNLED27351_SCAN_PHASE_10_CHANNEL'),
('MSKPHASE_9CHANNEL', 'SNLED27351_SCAN_PHASE_9_CHANNEL'),
('MSKPHASE_8CHANNEL', 'SNLED27351_SCAN_PHASE_8_CHANNEL'),
('MSKPHASE_7CHANNEL', 'SNLED27351_SCAN_PHASE_7_CHANNEL'),
('MSKPHASE_6CHANNEL', 'SNLED27351_SCAN_PHASE_6_CHANNEL'),
('MSKPHASE_5CHANNEL', 'SNLED27351_SCAN_PHASE_5_CHANNEL'),
('MSKPHASE_4CHANNEL', 'SNLED27351_SCAN_PHASE_4_CHANNEL'),
('MSKPHASE_3CHANNEL', 'SNLED27351_SCAN_PHASE_3_CHANNEL'),
('MSKPHASE_2CHANNEL', 'SNLED27351_SCAN_PHASE_2_CHANNEL'),
('MSKPHASE_1CHANNEL', 'SNLED27351_SCAN_PHASE_1_CHANNEL'),
#('#    define RGB_MATRIX_DRIVER_SHUTDOWN_ENABLE', '#    define RGB_MATRIX_DRIVER_SHUTDOWN_ENABLE\n#    define RGB_MATRIX_DRIVER_LOAD_ENABLE'),
#('#    define LED_MATRIX_DRIVER_SHUTDOWN_ENABLE', '#    define LED_MATRIX_DRIVER_SHUTDOWN_ENABLE\n#    define LED_MATRIX_DRIVER_LOAD_ENABLE'),
#(' *   |  |       G location', ' *   |  |           G location'),
#(' *   |  |       |       B location', ' *   |  |           |           B location'),
#(' *   |  |       |       | */', ' *   |  |           |           | */'),
#('CKLED', 'SNLED27351'),
('snled27351manual', 'SNLED27351 manual'),
('DRIVER_ADDR_1', 'SNLED27351_I2C_ADDRESS_1'),
('DRIVER_ADDR_2', 'SNLED27351_I2C_ADDRESS_2'),
('0b1110100', 'SNLED27351_I2C_ADDRESS_GND'),
('0b1110111', 'SNLED27351_I2C_ADDRESS_VDDIO'),
('#    define DRIVER_COUNT 2\n', ''),
('#    define DRIVER_COUNT 1\n', ''),
('extern uint8_t         g_pwm_buffer[DRIVER_COUNT][192];\n', ''),
#('#    define LED_MATRIX_DRIVER_LOAD_ENABLE\n#    define LED_MATRIX_DRIVER_LOAD_ENABLE\n#    define LED_MATRIX_DRIVER_LOAD_ENABLE\n#    define LED_MATRIX_DRIVER_LOAD_ENABLE', '#    define LED_MATRIX_DRIVER_LOAD_ENABLE'),
('encoders_pad_', 'encoders_pin_'),
('encoder_pad_', 'encoder_pin_'),
('encoder_pin_cb', 'encoders_pins_cb'),
('BT_HOST_LED_MATRIX_LIST', 'BT_INDCATION_LED_MATRIX_LIST'),
('BT_INDICATION_LED_LIST', 'BT_INDCATION_LED_MATRIX_LIST'),
('BT_HOST_LED_PIN_LIST', 'BT_INDICATION_LED_PIN_LIST'),
('P24G_HOST_LED_PIN_LIST', 'P24G_INDICATION_LED_PIN_LIST'),
('HOST_LED_PIN_LIST', 'BT_INDICATION_LED_PIN_LIST'),
('HOST_LED_MATRIX_LIST', 'BT_INDCATION_LED_MATRIX_LIST'),
('"task.h"', '"keychron_task.h"'),
('"common.h"', '"keychron_common.h"'),
('"wireless_common.h"', '"keychron_wireless_common.h"'),
('process_record_common', 'process_record_keychron_common'),
(' task_kb', ' keychron_task_kb'),
('/* Enable bluetooth NKRO */\n#    define WIRELESS_NKRO_ENABLE\n\n', ''),
]

# 需要排除的文件扩展名
exclude_extensions = {'.py', '.bin'}  # 在此处添加你想要排除的文件扩展名

def replace_in_file(filepath, replace_pairs):
    """在指定文件中根据提供的配对列表进行替换"""
    with open(filepath, 'r+', encoding='utf-8') as f:
        content = f.read()
        has_changes = False
        for old_str, new_str in replace_pairs:
            if old_str in content:
                content = content.replace(old_str, new_str)
                print(f"{filepath} 查找到 {old_str}")
                has_changes = True

        # 如果内容有变化，则写回文件
        if has_changes:
            f.seek(0)
            f.write(content)
            f.truncate()

def process_config_h(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False

    def check_and_modify(define_shutdown, define_load):
        nonlocal modified
        shutdown_enable_found = False
        load_enable_not_found = True

        for line in lines:
            if define_shutdown in line:
                shutdown_enable_found = True
            if define_load in line:
                load_enable_not_found = False

        if shutdown_enable_found and load_enable_not_found:
            for i, line in enumerate(lines):
                if define_shutdown in line:
                    lines.insert(i + 1, f"{define_load}\n")
                    modified = True
                    break

    # 检查并修改RGB_MATRIX相关定义
    check_and_modify('#    define RGB_MATRIX_DRIVER_SHUTDOWN_ENABLE', '#    define RGB_MATRIX_DRIVER_LOAD_ENABLE')
    # 检查并修改LED_MATRIX相关定义
    check_and_modify('#    define LED_MATRIX_DRIVER_SHUTDOWN_ENABLE', '#    define LED_MATRIX_DRIVER_LOAD_ENABLE')

    if modified:
        print(f"找到需要修改的config.h: {file_path}")
        try:
            with open(file_path, 'w') as file:
                file.writelines(lines)
            print(f"文件内容已更新: {file_path}")
        except Exception as e:
            print(f"更新文件内容时出错: {e}")

def process_files(directory):
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        # 检查是否包含info.json和keymap文件夹
        if 'info.json' in files and 'keymaps' in dirs:
            # 构造旧文件路径和新文件路径
            old_file_path = os.path.join(root, 'info.json')
            new_file_path = os.path.join(root, 'keyboard.json')

            print(f"找到匹配的info.json: {old_file_path}, 正在重命名...")

            # 重命名文件
            try:
                os.rename(old_file_path, new_file_path)
                print(f"文件已成功重命名为: {new_file_path}")
            except Exception as e:
                print(f"重命名文件时出错: {e}")

        # 处理rules.mk和post_rules.mk
        if 'post_rules.mk' in files:
            post_rules_path = os.path.join(root, 'post_rules.mk')
            print(f"找到并准备删除的post_rules.mk: {post_rules_path}")
            try:
                os.remove(post_rules_path)
                print(f"文件已成功删除: {post_rules_path}")
            except Exception as e:
                print(f"删除文件时出错: {e}")

        if 'rules.mk' in files:
            rules_mk_path = os.path.join(root, 'rules.mk')
            with open(rules_mk_path, 'r') as file:
                content = file.read()
            if 'keyboards/sub_brand/common/common.mk' in content:
                print(f"找到需要修改的rules.mk: {rules_mk_path}")
                new_content = """include keyboards/keychron/common/wireless/wireless.mk
include keyboards/keychron/common/keychron_common.mk

VPATH += $(TOP_DIR)/keyboards/keychron"""
                try:
                    with open(rules_mk_path, 'w') as file:
                        file.write(new_content)
                    print(f"文件内容已更新: {rules_mk_path}")
                except Exception as e:
                    print(f"更新文件内容时出错: {e}")

        # 查找config.h文件，并进行相应的修改
        if 'config.h' in files:
            config_h_path = os.path.join(root, 'config.h')
            process_config_h(config_h_path)


        # 获取文件扩展名并检查是否在排除列表中
        for filename in files:
            filepath = os.path.join(root, filename)
            # 获取文件扩展名并检查是否在排除列表中
            ext = os.path.splitext(filename)[1]
            if ext in exclude_extensions:
                #print(f"Skipping file: {filepath}")  # 输出被跳过的文件信息
                continue

            #print(f"Processing file: {filepath}")
            replace_in_file(filepath, replace_pairs)
            continue

if __name__ == "__main__":
    # 获取当前工作目录
    current_directory = os.getcwd()
    process_files(current_directory)
