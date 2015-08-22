#------------------------------------------------------------------------------ 
# Copyright (c) 2015 Ralph Hempel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ----------------------------------------------------------------------------u

#~autogen autogen-header 'py'>commentStyle -->
    # Sections of the following code were auto-generated based on spec v0.9.3-pre, rev 1. 

#~autogen

import os.path
import fnmatch

#------------------------------------------------------------------------------ 
# Define the base class from which all other ev3dev classes are defined.

global __EV3_MODULE_connected__
global __EV3_MODULE_attribute

__EV3_MODULE_connected__ = {} 

__EV3_MODULE_attribute__ = {}

class EV3_Device(object):
    """The ev3dev base class"""

    DEVICE_ROOT_PATH = '/sys/class'

    def __init__(self, class_name, port='auto', name_convention='' ):
        """Spin through the Linux sysfs class for the device type and find
           the first unconnected device"""
           
        self._classpath = os.path.abspath( EV3_Device.DEVICE_ROOT_PATH + '/' + class_name )
        
        if 'auto' == port:
            name = name_convention
        else:
            name = port

        for file in os.listdir( self._classpath ):
            if fnmatch.fnmatch(file, name):
                if file not in __EV3_MODULE_connected__:
                    __EV3_MODULE_connected__[file] = True
                    self._path = os.path.abspath( self._classpath + '/' + file )
                    print self._path
                    break

    def __attribute_name( self, attribute ):
        """Helper function that retuns the attribute path for a device"""
        attribute_name = os.path.abspath( self._path + '/' + attribute )
        if attribute_name not in __EV3_MODULE_attribute__:
            __EV3_MODULE_attribute__[attribute_name] = ''
            print 'Initializing ' + attribute_name
        return attribute_name

    def _get_attribute( self, attribute ):
        """Device attribute getter"""
        attribute_name = self.__attribute_name( attribute )
        print( 'Getting ' + attribute_name )
        return __EV3_MODULE_attribute__[attribute_name]

    def _set_attribute( self, attribute, value ):
        """Device attribute setter"""
        attribute_name = self.__attribute_name( attribute )
        print( 'Setting ' + attribute_name + ' to ' + value )
        __EV3_MODULE_attribute__[attribute_name] = value
        print __EV3_MODULE_attribute__[attribute_name] 

class Motor(EV3_Device):

#~autogen pure-python_generic-class-description classes.motor>currentClass
    """
    The motor class provides a uniform interface for using motors with
    positional and directional feedback such as the EV3 and NXT motors.
    This feedback allows for precise control of the motors. This is the
    most common type of motor, so we just call it `motor`.
    """

#~autogen

#   SYSTEM_CLASS_NAME = 'tacho-motor'
    SYSTEM_CLASS_NAME = 'tty'
    SYSTEM_CLASS_NAME_CONVENTION = 'ttyS*'

    def __init__(self, port='auto'):
        self._device = EV3_Device( Motor.SYSTEM_CLASS_NAME, port, Motor.SYSTEM_CLASS_NAME_CONVENTION )
#~autogen pure-python_generic-get-set classes.motor>currentClass


    def __set_command(self, value):
        self._device._set_attribute( 'command', value )

    __doc_command = (
        "Sends a command to the motor controller. See `commands` for a list of"
        "possible values."        )

    command = property( None, __set_command, None, __doc_command )

    def __get_commands(self):
        return self._device._get_attribute( 'commands' )

    __doc_commands = (
        "Returns a list of commands that are supported by the motor"
        "controller. Possible values are `run-forever`, `run-to-abs-pos`, `run-to-rel-pos`,"
        "`run-timed`, `run-direct`, `stop` and `reset`. Not all commands may be supported."
        "`run-forever` will cause the motor to run until another command is sent."
        "`run-to-abs-pos` will run to an absolute position specified by `position_sp`"
        "and then stop using the command specified in `stop_command`."
        "`run-to-rel-pos` will run to a position relative to the current `position` value."
        "The new position will be current `position` + `position_sp`. When the new"
        "position is reached, the motor will stop using the command specified by `stop_command`."
        "`run-timed` will run the motor for the amount of time specified in `time_sp`"
        "and then stop the motor using the command specified by `stop_command`."
        "`run-direct` will run the motor at the duty cycle specified by `duty_cycle_sp`."
        "Unlike other run commands, changing `duty_cycle_sp` while running *will*"
        "take effect immediately."
        "`stop` will stop any of the run commands before they are complete using the"
        "command specified by `stop_command`."
        "`reset` will reset all of the motor parameter attributes to their default value."
        "This will also have the effect of stopping the motor."        )

    commands = property( __get_commands, None, None, __doc_commands )

    def __get_count_per_rot(self):
        return self._device._get_attribute( 'count_per_rot' )

    __doc_count_per_rot = (
        "Returns the number of tacho counts in one rotation of the motor. Tacho counts"
        "are used by the position and speed attributes, so you can use this value"
        "to convert rotations or degrees to tacho counts. In the case of linear"
        "actuators, the units here will be counts per centimeter."        )

    count_per_rot = property( __get_count_per_rot, None, None, __doc_count_per_rot )

    def __get_driver_name(self):
        return self._device._get_attribute( 'driver_name' )

    __doc_driver_name = (
        "Returns the name of the driver that provides this tacho motor device."        )

    driver_name = property( __get_driver_name, None, None, __doc_driver_name )

    def __get_duty_cycle(self):
        return self._device._get_attribute( 'duty_cycle' )

    __doc_duty_cycle = (
        "Returns the current duty cycle of the motor. Units are percent. Values"
        "are -100 to 100."        )

    duty_cycle = property( __get_duty_cycle, None, None, __doc_duty_cycle )

    def __get_duty_cycle_sp(self):
        return self._device._get_attribute( 'duty_cycle_sp' )

    def __set_duty_cycle_sp(self, value):
        self._device._set_attribute( 'duty_cycle_sp', value )

    __doc_duty_cycle_sp = (
        "Writing sets the duty cycle setpoint. Reading returns the current value."
        "Units are in percent. Valid values are -100 to 100. A negative value causes"
        "the motor to rotate in reverse. This value is only used when `speed_regulation`"
        "is off."        )

    duty_cycle_sp = property( __get_duty_cycle_sp, __set_duty_cycle_sp, None, __doc_duty_cycle_sp )

    def __get_encoder_polarity(self):
        return self._device._get_attribute( 'encoder_polarity' )

    def __set_encoder_polarity(self, value):
        self._device._set_attribute( 'encoder_polarity', value )

    __doc_encoder_polarity = (
        "Sets the polarity of the rotary encoder. This is an advanced feature to all"
        "use of motors that send inversed encoder signals to the EV3. This should"
        "be set correctly by the driver of a device. It You only need to change this"
        "value if you are using a unsupported device. Valid values are `normal` and"
        "`inversed`."        )

    encoder_polarity = property( __get_encoder_polarity, __set_encoder_polarity, None, __doc_encoder_polarity )

    def __get_polarity(self):
        return self._device._get_attribute( 'polarity' )

    def __set_polarity(self, value):
        self._device._set_attribute( 'polarity', value )

    __doc_polarity = (
        "Sets the polarity of the motor. With `normal` polarity, a positive duty"
        "cycle will cause the motor to rotate clockwise. With `inversed` polarity,"
        "a positive duty cycle will cause the motor to rotate counter-clockwise."
        "Valid values are `normal` and `inversed`."        )

    polarity = property( __get_polarity, __set_polarity, None, __doc_polarity )

    def __get_port_name(self):
        return self._device._get_attribute( 'port_name' )

    __doc_port_name = (
        "Returns the name of the port that the motor is connected to."        )

    port_name = property( __get_port_name, None, None, __doc_port_name )

    def __get_position(self):
        return self._device._get_attribute( 'position' )

    def __set_position(self, value):
        self._device._set_attribute( 'position', value )

    __doc_position = (
        "Returns the current position of the motor in pulses of the rotary"
        "encoder. When the motor rotates clockwise, the position will increase."
        "Likewise, rotating counter-clockwise causes the position to decrease."
        "Writing will set the position to that value."        )

    position = property( __get_position, __set_position, None, __doc_position )

    def __get_position_p(self):
        return self._device._get_attribute( 'position_p' )

    def __set_position_p(self, value):
        self._device._set_attribute( 'position_p', value )

    __doc_position_p = (
        "The proportional constant for the position PID."        )

    position_p = property( __get_position_p, __set_position_p, None, __doc_position_p )

    def __get_position_i(self):
        return self._device._get_attribute( 'position_i' )

    def __set_position_i(self, value):
        self._device._set_attribute( 'position_i', value )

    __doc_position_i = (
        "The integral constant for the position PID."        )

    position_i = property( __get_position_i, __set_position_i, None, __doc_position_i )

    def __get_position_d(self):
        return self._device._get_attribute( 'position_d' )

    def __set_position_d(self, value):
        self._device._set_attribute( 'position_d', value )

    __doc_position_d = (
        "The derivative constant for the position PID."        )

    position_d = property( __get_position_d, __set_position_d, None, __doc_position_d )

    def __get_position_sp(self):
        return self._device._get_attribute( 'position_sp' )

    def __set_position_sp(self, value):
        self._device._set_attribute( 'position_sp', value )

    __doc_position_sp = (
        "Writing specifies the target position for the `run-to-abs-pos` and `run-to-rel-pos`"
        "commands. Reading returns the current value. Units are in tacho counts. You"
        "can use the value returned by `counts_per_rot` to convert tacho counts to/from"
        "rotations or degrees."        )

    position_sp = property( __get_position_sp, __set_position_sp, None, __doc_position_sp )

    def __get_speed(self):
        return self._device._get_attribute( 'speed' )

    __doc_speed = (
        "Returns the current motor speed in tacho counts per second. Not, this is"
        "not necessarily degrees (although it is for LEGO motors). Use the `count_per_rot`"
        "attribute to convert this value to RPM or deg/sec."        )

    speed = property( __get_speed, None, None, __doc_speed )

    def __get_speed_sp(self):
        return self._device._get_attribute( 'speed_sp' )

    def __set_speed_sp(self, value):
        self._device._set_attribute( 'speed_sp', value )

    __doc_speed_sp = (
        "Writing sets the target speed in tacho counts per second used when `speed_regulation`"
        "is on. Reading returns the current value.  Use the `count_per_rot` attribute"
        "to convert RPM or deg/sec to tacho counts per second."        )

    speed_sp = property( __get_speed_sp, __set_speed_sp, None, __doc_speed_sp )

    def __get_ramp_up_sp(self):
        return self._device._get_attribute( 'ramp_up_sp' )

    def __set_ramp_up_sp(self, value):
        self._device._set_attribute( 'ramp_up_sp', value )

    __doc_ramp_up_sp = (
        "Writing sets the ramp up setpoint. Reading returns the current value. Units"
        "are in milliseconds. When set to a value > 0, the motor will ramp the power"
        "sent to the motor from 0 to 100% duty cycle over the span of this setpoint"
        "when starting the motor. If the maximum duty cycle is limited by `duty_cycle_sp`"
        "or speed regulation, the actual ramp time duration will be less than the setpoint."        )

    ramp_up_sp = property( __get_ramp_up_sp, __set_ramp_up_sp, None, __doc_ramp_up_sp )

    def __get_ramp_down_sp(self):
        return self._device._get_attribute( 'ramp_down_sp' )

    def __set_ramp_down_sp(self, value):
        self._device._set_attribute( 'ramp_down_sp', value )

    __doc_ramp_down_sp = (
        "Writing sets the ramp down setpoint. Reading returns the current value. Units"
        "are in milliseconds. When set to a value > 0, the motor will ramp the power"
        "sent to the motor from 100% duty cycle down to 0 over the span of this setpoint"
        "when stopping the motor. If the starting duty cycle is less than 100%, the"
        "ramp time duration will be less than the full span of the setpoint."        )

    ramp_down_sp = property( __get_ramp_down_sp, __set_ramp_down_sp, None, __doc_ramp_down_sp )

    def __get_speed_regulation_enabled(self):
        return self._device._get_attribute( 'speed_regulation_enabled' )

    def __set_speed_regulation_enabled(self, value):
        self._device._set_attribute( 'speed_regulation_enabled', value )

    __doc_speed_regulation_enabled = (
        "Turns speed regulation on or off. If speed regulation is on, the motor"
        "controller will vary the power supplied to the motor to try to maintain the"
        "speed specified in `speed_sp`. If speed regulation is off, the controller"
        "will use the power specified in `duty_cycle_sp`. Valid values are `on` and"
        "`off`."        )

    speed_regulation_enabled = property( __get_speed_regulation_enabled, __set_speed_regulation_enabled, None, __doc_speed_regulation_enabled )

    def __get_speed_regulation_p(self):
        return self._device._get_attribute( 'speed_regulation_p' )

    def __set_speed_regulation_p(self, value):
        self._device._set_attribute( 'speed_regulation_p', value )

    __doc_speed_regulation_p = (
        "The proportional constant for the speed regulation PID."        )

    speed_regulation_p = property( __get_speed_regulation_p, __set_speed_regulation_p, None, __doc_speed_regulation_p )

    def __get_speed_regulation_i(self):
        return self._device._get_attribute( 'speed_regulation_i' )

    def __set_speed_regulation_i(self, value):
        self._device._set_attribute( 'speed_regulation_i', value )

    __doc_speed_regulation_i = (
        "The integral constant for the speed regulation PID."        )

    speed_regulation_i = property( __get_speed_regulation_i, __set_speed_regulation_i, None, __doc_speed_regulation_i )

    def __get_speed_regulation_d(self):
        return self._device._get_attribute( 'speed_regulation_d' )

    def __set_speed_regulation_d(self, value):
        self._device._set_attribute( 'speed_regulation_d', value )

    __doc_speed_regulation_d = (
        "The derivative constant for the speed regulation PID."        )

    speed_regulation_d = property( __get_speed_regulation_d, __set_speed_regulation_d, None, __doc_speed_regulation_d )

    def __get_state(self):
        return self._device._get_attribute( 'state' )

    __doc_state = (
        "Reading returns a list of state flags. Possible flags are"
        "`running`, `ramping` `holding` and `stalled`."        )

    state = property( __get_state, None, None, __doc_state )

    def __get_stop_command(self):
        return self._device._get_attribute( 'stop_command' )

    def __set_stop_command(self, value):
        self._device._set_attribute( 'stop_command', value )

    __doc_stop_command = (
        "Reading returns the current stop command. Writing sets the stop command."
        "The value determines the motors behavior when `command` is set to `stop`."
        "Also, it determines the motors behavior when a run command completes. See"
        "`stop_commands` for a list of possible values."        )

    stop_command = property( __get_stop_command, __set_stop_command, None, __doc_stop_command )

    def __get_stop_commands(self):
        return self._device._get_attribute( 'stop_commands' )

    __doc_stop_commands = (
        "Returns a list of stop modes supported by the motor controller."
        "Possible values are `coast`, `brake` and `hold`. `coast` means that power will"
        "be removed from the motor and it will freely coast to a stop. `brake` means"
        "that power will be removed from the motor and a passive electrical load will"
        "be placed on the motor. This is usually done by shorting the motor terminals"
        "together. This load will absorb the energy from the rotation of the motors and"
        "cause the motor to stop more quickly than coasting. `hold` does not remove"
        "power from the motor. Instead it actively try to hold the motor at the current"
        "position. If an external force tries to turn the motor, the motor will 'push"
        "back' to maintain its position."        )

    stop_commands = property( __get_stop_commands, None, None, __doc_stop_commands )

    def __get_time_sp(self):
        return self._device._get_attribute( 'time_sp' )

    def __set_time_sp(self, value):
        self._device._set_attribute( 'time_sp', value )

    __doc_time_sp = (
        "Writing specifies the amount of time the motor will run when using the"
        "`run-timed` command. Reading returns the current value. Units are in"
        "milliseconds."        )

    time_sp = property( __get_time_sp, __set_time_sp, None, __doc_time_sp )


#~autogen

motor1 = Motor()
motor2 = Motor('ttyS3')
motor3 = Motor()

motor1.command = 'foo'
motor2.command = 'bar'
motor3.command = '0' 

print motor1.duty_cycle_sp
motor1.duty_cycle_sp = '50'
print motor1.duty_cycle_sp

if 0:

#~autogen pure-python_generic-property-value classes.motor>currentClass


    __propval_command = {  
      'run-forever':'Run the motor until another command is sent.' , 
      'run-to-abs-pos':'Run to an absolute position specified by `position_sp` and thenstop using the command specified in `stop_command`.' , 
      'run-to-rel-pos':'Run to a position relative to the current `position` value.The new position will be current `position` + `position_sp`.When the new position is reached, the motor will stop usingthe command specified by `stop_command`.' , 
      'run-timed':'Run the motor for the amount of time specified in `time_sp`and then stop the motor using the command specified by `stop_command`.' , 
      'run-direct':'Run the motor at the duty cycle specified by `duty_cycle_sp`.Unlike other run commands, changing `duty_cycle_sp` while running *will*take effect immediately.' , 
      'stop':'Stop any of the run commands before they are complete using thecommand specified by `stop_command`.' , 
      'reset':'Reset all of the motor parameter attributes to their default value.This will also have the effect of stopping the motor.' ,
          }

    __propval_encoder_polarity = {  
      'normal':'Sets the normal polarity of the rotary encoder.' , 
      'inversed':'Sets the inversed polarity of the rotary encoder.' ,
          }

    __propval_polarity = {  
      'normal':'With `normal` polarity, a positive duty cycle willcause the motor to rotate clockwise.' , 
      'inversed':'With `inversed` polarity, a positive duty cycle willcause the motor to rotate counter-clockwise.' ,
          }

    __propval_speed_regulation = {  
      'on':'The motor controller will vary the power supplied to the motorto try to maintain the speed specified in `speed_sp`.' , 
      'off':'The motor controller will use the power specified in `duty_cycle_sp`.' ,
          }

    __propval_stop_command = {  
      'coast':'Power will be removed from the motor and it will freely coast to a stop.' , 
      'brake':'Power will be removed from the motor and a passive electrical load willbe placed on the motor. This is usually done by shorting the motor terminalstogether. This load will absorb the energy from the rotation of the motors andcause the motor to stop more quickly than coasting.' , 
      'hold':'Does not remove power from the motor. Instead it actively try to hold the motorat the current position. If an external force tries to turn the motor, the motorwill ``push back`` to maintain its position.' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.dcMotor>currentClass
    """
    The DC motor class provides a uniform interface for using regular DC motors
    with no fancy controls or feedback. This includes LEGO MINDSTORMS RCX motors
    and LEGO Power Functions motors.
    """

#~autogen
#~autogen pure-python_generic-get-set classes.dcMotor>currentClass


    def __set_command(self, value):
        self._device._set_attribute( 'command', value )

    __doc_command = (
        "Sets the command for the motor. Possible values are `run-forever`, `run-timed` and"
        "`stop`. Not all commands may be supported, so be sure to check the contents"
        "of the `commands` attribute."        )

    command = property( None, __set_command, None, __doc_command )

    def __get_commands(self):
        return self._device._get_attribute( 'commands' )

    __doc_commands = (
        "Returns a list of commands supported by the motor"
        "controller."        )

    commands = property( __get_commands, None, None, __doc_commands )

    def __get_driver_name(self):
        return self._device._get_attribute( 'driver_name' )

    __doc_driver_name = (
        "Returns the name of the motor driver that loaded this device. See the list"
        "of [supported devices] for a list of drivers."        )

    driver_name = property( __get_driver_name, None, None, __doc_driver_name )

    def __get_duty_cycle(self):
        return self._device._get_attribute( 'duty_cycle' )

    __doc_duty_cycle = (
        "Shows the current duty cycle of the PWM signal sent to the motor. Values"
        "are -100 to 100 (-100% to 100%)."        )

    duty_cycle = property( __get_duty_cycle, None, None, __doc_duty_cycle )

    def __get_duty_cycle_sp(self):
        return self._device._get_attribute( 'duty_cycle_sp' )

    def __set_duty_cycle_sp(self, value):
        self._device._set_attribute( 'duty_cycle_sp', value )

    __doc_duty_cycle_sp = (
        "Writing sets the duty cycle setpoint of the PWM signal sent to the motor."
        "Valid values are -100 to 100 (-100% to 100%). Reading returns the current"
        "setpoint."        )

    duty_cycle_sp = property( __get_duty_cycle_sp, __set_duty_cycle_sp, None, __doc_duty_cycle_sp )

    def __get_polarity(self):
        return self._device._get_attribute( 'polarity' )

    def __set_polarity(self, value):
        self._device._set_attribute( 'polarity', value )

    __doc_polarity = (
        "Sets the polarity of the motor. Valid values are `normal` and `inversed`."        )

    polarity = property( __get_polarity, __set_polarity, None, __doc_polarity )

    def __get_port_name(self):
        return self._device._get_attribute( 'port_name' )

    __doc_port_name = (
        "Returns the name of the port that the motor is connected to."        )

    port_name = property( __get_port_name, None, None, __doc_port_name )

    def __get_ramp_down_sp(self):
        return self._device._get_attribute( 'ramp_down_sp' )

    def __set_ramp_down_sp(self, value):
        self._device._set_attribute( 'ramp_down_sp', value )

    __doc_ramp_down_sp = (
        "Sets the time in milliseconds that it take the motor to ramp down from 100%"
        "to 0%. Valid values are 0 to 10000 (10 seconds). Default is 0."        )

    ramp_down_sp = property( __get_ramp_down_sp, __set_ramp_down_sp, None, __doc_ramp_down_sp )

    def __get_ramp_up_sp(self):
        return self._device._get_attribute( 'ramp_up_sp' )

    def __set_ramp_up_sp(self, value):
        self._device._set_attribute( 'ramp_up_sp', value )

    __doc_ramp_up_sp = (
        "Sets the time in milliseconds that it take the motor to up ramp from 0% to"
        "100%. Valid values are 0 to 10000 (10 seconds). Default is 0."        )

    ramp_up_sp = property( __get_ramp_up_sp, __set_ramp_up_sp, None, __doc_ramp_up_sp )

    def __get_state(self):
        return self._device._get_attribute( 'state' )

    __doc_state = (
        "Gets a list of flags indicating the motor status. Possible"
        "flags are `running` and `ramping`. `running` indicates that the motor is"
        "powered. `ramping` indicates that the motor has not yet reached the"
        "`duty_cycle_sp`."        )

    state = property( __get_state, None, None, __doc_state )

    def __set_stop_command(self, value):
        self._device._set_attribute( 'stop_command', value )

    __doc_stop_command = (
        "Sets the stop command that will be used when the motor stops. Read"
        "`stop_commands` to get the list of valid values."        )

    stop_command = property( None, __set_stop_command, None, __doc_stop_command )

    def __get_stop_commands(self):
        return self._device._get_attribute( 'stop_commands' )

    __doc_stop_commands = (
        "Gets a list of stop commands. Valid values are `coast`"
        "and `brake`."        )

    stop_commands = property( __get_stop_commands, None, None, __doc_stop_commands )


#~autogen
#~autogen pure-python_generic-property-value classes.dcMotor>currentClass


    __propval_command = {  
      'run-forever':'Run the motor until another command is sent.' , 
      'run-timed':'Run the motor for the amount of time specified in `time_sp`and then stop the motor using the command specified by `stop_command`.' , 
      'stop':'Stop any of the run commands before they are complete using thecommand specified by `stop_command`.' ,
          }

    __propval_polarity = {  
      'normal':'With `normal` polarity, a positive duty cycle willcause the motor to rotate clockwise.' , 
      'inversed':'With `inversed` polarity, a positive duty cycle willcause the motor to rotate counter-clockwise.' ,
          }

    __propval_stop_command = {  
      'coast':'Power will be removed from the motor and it will freely coast to a stop.' , 
      'brake':'Power will be removed from the motor and a passive electrical load willbe placed on the motor. This is usually done by shorting the motor terminalstogether. This load will absorb the energy from the rotation of the motors andcause the motor to stop more quickly than coasting.' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.servoMotor>currentClass
    """
    The servo motor class provides a uniform interface for using hobby type
    servo motors.
    """

#~autogen
#~autogen pure-python_generic-get-set classes.servoMotor>currentClass


    def __set_command(self, value):
        self._device._set_attribute( 'command', value )

    __doc_command = (
        "Sets the command for the servo. Valid values are `run` and `float`. Setting"
        "to `run` will cause the servo to be driven to the position_sp set in the"
        "`position_sp` attribute. Setting to `float` will remove power from the motor."        )

    command = property( None, __set_command, None, __doc_command )

    def __get_driver_name(self):
        return self._device._get_attribute( 'driver_name' )

    __doc_driver_name = (
        "Returns the name of the motor driver that loaded this device. See the list"
        "of [supported devices] for a list of drivers."        )

    driver_name = property( __get_driver_name, None, None, __doc_driver_name )

    def __get_max_pulse_sp(self):
        return self._device._get_attribute( 'max_pulse_sp' )

    def __set_max_pulse_sp(self, value):
        self._device._set_attribute( 'max_pulse_sp', value )

    __doc_max_pulse_sp = (
        "Used to set the pulse size in milliseconds for the signal that tells the"
        "servo to drive to the maximum (clockwise) position_sp. Default value is 2400."
        "Valid values are 2300 to 2700. You must write to the position_sp attribute for"
        "changes to this attribute to take effect."        )

    max_pulse_sp = property( __get_max_pulse_sp, __set_max_pulse_sp, None, __doc_max_pulse_sp )

    def __get_mid_pulse_sp(self):
        return self._device._get_attribute( 'mid_pulse_sp' )

    def __set_mid_pulse_sp(self, value):
        self._device._set_attribute( 'mid_pulse_sp', value )

    __doc_mid_pulse_sp = (
        "Used to set the pulse size in milliseconds for the signal that tells the"
        "servo to drive to the mid position_sp. Default value is 1500. Valid"
        "values are 1300 to 1700. For example, on a 180 degree servo, this would be"
        "90 degrees. On continuous rotation servo, this is the 'neutral' position_sp"
        "where the motor does not turn. You must write to the position_sp attribute for"
        "changes to this attribute to take effect."        )

    mid_pulse_sp = property( __get_mid_pulse_sp, __set_mid_pulse_sp, None, __doc_mid_pulse_sp )

    def __get_min_pulse_sp(self):
        return self._device._get_attribute( 'min_pulse_sp' )

    def __set_min_pulse_sp(self, value):
        self._device._set_attribute( 'min_pulse_sp', value )

    __doc_min_pulse_sp = (
        "Used to set the pulse size in milliseconds for the signal that tells the"
        "servo to drive to the miniumum (counter-clockwise) position_sp. Default value"
        "is 600. Valid values are 300 to 700. You must write to the position_sp"
        "attribute for changes to this attribute to take effect."        )

    min_pulse_sp = property( __get_min_pulse_sp, __set_min_pulse_sp, None, __doc_min_pulse_sp )

    def __get_polarity(self):
        return self._device._get_attribute( 'polarity' )

    def __set_polarity(self, value):
        self._device._set_attribute( 'polarity', value )

    __doc_polarity = (
        "Sets the polarity of the servo. Valid values are `normal` and `inversed`."
        "Setting the value to `inversed` will cause the position_sp value to be"
        "inversed. i.e `-100` will correspond to `max_pulse_sp`, and `100` will"
        "correspond to `min_pulse_sp`."        )

    polarity = property( __get_polarity, __set_polarity, None, __doc_polarity )

    def __get_port_name(self):
        return self._device._get_attribute( 'port_name' )

    __doc_port_name = (
        "Returns the name of the port that the motor is connected to."        )

    port_name = property( __get_port_name, None, None, __doc_port_name )

    def __get_position_sp(self):
        return self._device._get_attribute( 'position_sp' )

    def __set_position_sp(self, value):
        self._device._set_attribute( 'position_sp', value )

    __doc_position_sp = (
        "Reading returns the current position_sp of the servo. Writing instructs the"
        "servo to move to the specified position_sp. Units are percent. Valid values"
        "are -100 to 100 (-100% to 100%) where `-100` corresponds to `min_pulse_sp`,"
        "`0` corresponds to `mid_pulse_sp` and `100` corresponds to `max_pulse_sp`."        )

    position_sp = property( __get_position_sp, __set_position_sp, None, __doc_position_sp )

    def __get_rate_sp(self):
        return self._device._get_attribute( 'rate_sp' )

    def __set_rate_sp(self, value):
        self._device._set_attribute( 'rate_sp', value )

    __doc_rate_sp = (
        "Sets the rate_sp at which the servo travels from 0 to 100.0% (half of the full"
        "range of the servo). Units are in milliseconds. Example: Setting the rate_sp"
        "to 1000 means that it will take a 180 degree servo 2 second to move from 0"
        "to 180 degrees. Note: Some servo controllers may not support this in which"
        "case reading and writing will fail with `-EOPNOTSUPP`. In continuous rotation"
        "servos, this value will affect the rate_sp at which the speed ramps up or down."        )

    rate_sp = property( __get_rate_sp, __set_rate_sp, None, __doc_rate_sp )

    def __get_state(self):
        return self._device._get_attribute( 'state' )

    __doc_state = (
        "Returns a list of flags indicating the state of the servo."
        "Possible values are:"
        "* `running`: Indicates that the motor is powered."        )

    state = property( __get_state, None, None, __doc_state )


#~autogen
#~autogen pure-python_generic-property-value classes.servoMotor>currentClass


    __propval_command = {  
      'run':'Drive servo to the position set in the `position_sp` attribute.' , 
      'float':'Remove power from the motor.' ,
          }

    __propval_polarity = {  
      'normal':'With `normal` polarity, a positive duty cycle willcause the motor to rotate clockwise.' , 
      'inversed':'With `inversed` polarity, a positive duty cycle willcause the motor to rotate counter-clockwise.' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.sensor>currentClass
    """
    The sensor class provides a uniform interface for using most of the
    sensors available for the EV3. The various underlying device drivers will
    create a `lego-sensor` device for interacting with the sensors.
    
    Sensors are primarily controlled by setting the `mode` and monitored by
    reading the `value<N>` attributes. Values can be converted to floating point
    if needed by `value<N>` / 10.0 ^ `decimals`.
    
    Since the name of the `sensor<N>` device node does not correspond to the port
    that a sensor is plugged in to, you must look at the `port_name` attribute if
    you need to know which port a sensor is plugged in to. However, if you don't
    have more than one sensor of each type, you can just look for a matching
    `driver_name`. Then it will not matter which port a sensor is plugged in to - your
    program will still work.
    """

#~autogen



#~autogen pure-python_generic-get-set classes.sensor>currentClass


    def __set_command(self, value):
        self._device._set_attribute( 'command', value )

    __doc_command = (
        "Sends a command to the sensor."        )

    command = property( None, __set_command, None, __doc_command )

    def __get_commands(self):
        return self._device._get_attribute( 'commands' )

    __doc_commands = (
        "Returns a list of the valid commands for the sensor."
        "Returns -EOPNOTSUPP if no commands are supported."        )

    commands = property( __get_commands, None, None, __doc_commands )

    def __get_decimals(self):
        return self._device._get_attribute( 'decimals' )

    __doc_decimals = (
        "Returns the number of decimal places for the values in the `value<N>`"
        "attributes of the current mode."        )

    decimals = property( __get_decimals, None, None, __doc_decimals )

    def __get_driver_name(self):
        return self._device._get_attribute( 'driver_name' )

    __doc_driver_name = (
        "Returns the name of the sensor device/driver. See the list of [supported"
        "sensors] for a complete list of drivers."        )

    driver_name = property( __get_driver_name, None, None, __doc_driver_name )

    def __get_mode(self):
        return self._device._get_attribute( 'mode' )

    def __set_mode(self, value):
        self._device._set_attribute( 'mode', value )

    __doc_mode = (
        "Returns the current mode. Writing one of the values returned by `modes`"
        "sets the sensor to that mode."        )

    mode = property( __get_mode, __set_mode, None, __doc_mode )

    def __get_modes(self):
        return self._device._get_attribute( 'modes' )

    __doc_modes = (
        "Returns a list of the valid modes for the sensor."        )

    modes = property( __get_modes, None, None, __doc_modes )

    def __get_num_values(self):
        return self._device._get_attribute( 'num_values' )

    __doc_num_values = (
        "Returns the number of `value<N>` attributes that will return a valid value"
        "for the current mode."        )

    num_values = property( __get_num_values, None, None, __doc_num_values )

    def __get_port_name(self):
        return self._device._get_attribute( 'port_name' )

    __doc_port_name = (
        "Returns the name of the port that the sensor is connected to, e.g. `ev3:in1`."
        "I2C sensors also include the I2C address (decimal), e.g. `ev3:in1:i2c8`."        )

    port_name = property( __get_port_name, None, None, __doc_port_name )

    def __get_units(self):
        return self._device._get_attribute( 'units' )

    __doc_units = (
        "Returns the units of the measured value for the current mode. May return"
        "empty string"        )

    units = property( __get_units, None, None, __doc_units )


#~autogen
#~autogen pure-python_generic-class-description classes.i2cSensor>currentClass
    """
    A generic interface to control I2C-type EV3 sensors.
    """

#~autogen
#~autogen pure-python_generic-get-set classes.i2cSensor>currentClass


    def __get_fw_version(self):
        return self._device._get_attribute( 'fw_version' )

    __doc_fw_version = (
        "Returns the firmware version of the sensor if available. Currently only"
        "I2C/NXT sensors support this."        )

    fw_version = property( __get_fw_version, None, None, __doc_fw_version )

    def __get_poll_ms(self):
        return self._device._get_attribute( 'poll_ms' )

    def __set_poll_ms(self, value):
        self._device._set_attribute( 'poll_ms', value )

    __doc_poll_ms = (
        "Returns the polling period of the sensor in milliseconds. Writing sets the"
        "polling period. Setting to 0 disables polling. Minimum value is hard"
        "coded as 50 msec. Returns -EOPNOTSUPP if changing polling is not supported."
        "Currently only I2C/NXT sensors support changing the polling period."        )

    poll_ms = property( __get_poll_ms, __set_poll_ms, None, __doc_poll_ms )


#~autogen
#~autogen pure-python_generic-class-description classes.colorSensor>currentClass
    """
    LEGO EV3 color sensor.
    """

#~autogen
#~autogen pure-python_generic-property-value classes.colorSensor>currentClass


    __propval_mode = {  
      'COL-REFLECT':'Reflected light. Red LED on.' , 
      'COL-AMBIENT':'Ambient light. Red LEDs off.' , 
      'COL-COLOR':'Color. All LEDs rapidly cycling, appears white.' , 
      'REF-RAW':'Raw reflected. Red LED on' , 
      'RGB-RAW':'Raw Color Components. All LEDs rapidly cycling, appears white.' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.ultrasonicSensor>currentClass
    """
    LEGO EV3 ultrasonic sensor.
    """

#~autogen
#~autogen pure-python_generic-property-value classes.ultrasonicSensor>currentClass


    __propval_mode = {  
      'US-DIST-CM':'Continuous measurement in centimeters.LEDs: On, steady' , 
      'US-DIST-IN':'Continuous measurement in inches.LEDs: On, steady' , 
      'US-LISTEN':'Listen.  LEDs: On, blinking' , 
      'US-SI-CM':'Single measurement in centimeters.LEDs: On momentarily when mode is set, then off' , 
      'US-SI-IN':'Single measurement in inches.LEDs: On momentarily when mode is set, then off' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.gyroSensor>currentClass
    """
    LEGO EV3 gyro sensor.
    """

#~autogen
#~autogen pure-python_generic-property-value classes.gyroSensor>currentClass


    __propval_mode = {  
      'GYRO-ANG':'Angle' , 
      'GYRO-RATE':'Rotational speed' , 
      'GYRO-FAS':'Raw sensor value' , 
      'GYRO-G&A':'Angle and rotational speed' , 
      'GYRO-CAL':'Calibration ???' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.infraredSensor>currentClass
    """
    LEGO EV3 infrared sensor.
    """

#~autogen
#~autogen pure-python_generic-property-value classes.infraredSensor>currentClass


    __propval_mode = {  
      'IR-PROX':'Proximity' , 
      'IR-SEEK':'IR Seeker' , 
      'IR-REMOTE':'IR Remote Control' , 
      'IR-REM-A':'IR Remote Control. State of the buttons is coded in binary' , 
      'IR-CAL':'Calibration ???' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.soundSensor>currentClass
    """
    LEGO NXT Sound Sensor
    """

#~autogen
#~autogen pure-python_generic-property-value classes.soundSensor>currentClass


    __propval_mode = {  
      'DB':'Sound pressure level. Flat weighting' , 
      'DBA':'Sound pressure level. A weighting' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.lightSensor>currentClass
    """
    LEGO NXT Light Sensor
    """

#~autogen
#~autogen pure-python_generic-property-value classes.lightSensor>currentClass


    __propval_mode = {  
      'REFLECT':'Reflected light. LED on' , 
      'AMBIENT':'Ambient light. LED off' ,
          }

#~autogen
#~autogen pure-python_generic-class-description classes.led>currentClass
    """
    Any device controlled by the generic LED driver.
    See https://www.kernel.org/doc/Documentation/leds/leds-class.txt
    for more details.
    """

#~autogen
#~autogen pure-python_generic-get-set classes.led>currentClass


    def __get_max_brightness(self):
        return self._device._get_attribute( 'max_brightness' )

    __doc_max_brightness = (
        "Returns the maximum allowable brightness value."        )

    max_brightness = property( __get_max_brightness, None, None, __doc_max_brightness )

    def __get_brightness(self):
        return self._device._get_attribute( 'brightness' )

    def __set_brightness(self, value):
        self._device._set_attribute( 'brightness', value )

    __doc_brightness = (
        "Sets the brightness level. Possible values are from 0 to `max_brightness`."        )

    brightness = property( __get_brightness, __set_brightness, None, __doc_brightness )

    def __get_triggers(self):
        return self._device._get_attribute( 'triggers' )

    __doc_triggers = (
        "Returns a list of available triggers."        )

    triggers = property( __get_triggers, None, None, __doc_triggers )

    def __get_trigger(self):
        return self._device._get_attribute( 'trigger' )

    def __set_trigger(self, value):
        self._device._set_attribute( 'trigger', value )

    __doc_trigger = (
        "Sets the led trigger. A trigger"
        "is a kernel based source of led events. Triggers can either be simple or"
        "complex. A simple trigger isn't configurable and is designed to slot into"
        "existing subsystems with minimal additional code. Examples are the `ide-disk` and"
        "`nand-disk` triggers."
        ""
        "Complex triggers whilst available to all LEDs have LED specific"
        "parameters and work on a per LED basis. The `timer` trigger is an example."
        "The `timer` trigger will periodically change the LED brightness between"
        "0 and the current brightness setting. The `on` and `off` time can"
        "be specified via `delay_{on,off}` attributes in milliseconds."
        "You can change the brightness value of a LED independently of the timer"
        "trigger. However, if you set the brightness value to 0 it will"
        "also disable the `timer` trigger."        )

    trigger = property( __get_trigger, __set_trigger, None, __doc_trigger )

    def __get_delay_on(self):
        return self._device._get_attribute( 'delay_on' )

    def __set_delay_on(self, value):
        self._device._set_attribute( 'delay_on', value )

    __doc_delay_on = (
        "The `timer` trigger will periodically change the LED brightness between"
        "0 and the current brightness setting. The `on` time can"
        "be specified via `delay_on` attribute in milliseconds."        )

    delay_on = property( __get_delay_on, __set_delay_on, None, __doc_delay_on )

    def __get_delay_off(self):
        return self._device._get_attribute( 'delay_off' )

    def __set_delay_off(self, value):
        self._device._set_attribute( 'delay_off', value )

    __doc_delay_off = (
        "The `timer` trigger will periodically change the LED brightness between"
        "0 and the current brightness setting. The `off` time can"
        "be specified via `delay_off` attribute in milliseconds."        )

    delay_off = property( __get_delay_off, __set_delay_off, None, __doc_delay_off )


#~autogen
#~autogen pure-python_generic-class-description classes.powerSupply>currentClass
    """
    A generic interface to read data from the system's power_supply class.
    Uses the built-in legoev3-battery if none is specified.
    """

#~autogen
#~autogen pure-python_generic-get-set classes.powerSupply>currentClass


    def __get_measured_current(self):
        return self._device._get_attribute( 'measured_current' )

    __doc_measured_current = (
        "The measured current that the battery is supplying (in microamps)"        )

    measured_current = property( __get_measured_current, None, None, __doc_measured_current )

    def __get_measured_voltage(self):
        return self._device._get_attribute( 'measured_voltage' )

    __doc_measured_voltage = (
        "The measured voltage that the battery is supplying (in microvolts)"        )

    measured_voltage = property( __get_measured_voltage, None, None, __doc_measured_voltage )

    def __get_max_voltage(self):
        return self._device._get_attribute( 'max_voltage' )

    __doc_max_voltage = (        )

    max_voltage = property( __get_max_voltage, None, None, __doc_max_voltage )

    def __get_min_voltage(self):
        return self._device._get_attribute( 'min_voltage' )

    __doc_min_voltage = (        )

    min_voltage = property( __get_min_voltage, None, None, __doc_min_voltage )

    def __get_technology(self):
        return self._device._get_attribute( 'technology' )

    __doc_technology = (        )

    technology = property( __get_technology, None, None, __doc_technology )

    def __get_type(self):
        return self._device._get_attribute( 'type' )

    __doc_type = (        )

    type = property( __get_type, None, None, __doc_type )


#~autogen
#~autogen pure-python_generic-class-description classes.legoPort>currentClass
    """
    The `lego-port` class provides an interface for working with input and
    output ports that are compatible with LEGO MINDSTORMS RCX/NXT/EV3, LEGO
    WeDo and LEGO Power Functions sensors and motors. Supported devices include
    the LEGO MINDSTORMS EV3 Intelligent Brick, the LEGO WeDo USB hub and
    various sensor multiplexers from 3rd party manufacturers.
    
    Some types of ports may have multiple modes of operation. For example, the
    input ports on the EV3 brick can communicate with sensors using UART, I2C
    or analog validate signals - but not all at the same time. Therefore there
    are multiple modes available to connect to the different types of sensors.
    
    In most cases, ports are able to automatically detect what type of sensor
    or motor is connected. In some cases though, this must be manually specified
    using the `mode` and `set_device` attributes. The `mode` attribute affects
    how the port communicates with the connected device. For example the input
    ports on the EV3 brick can communicate using UART, I2C or analog voltages,
    but not all at the same time, so the mode must be set to the one that is
    appropriate for the connected sensor. The `set_device` attribute is used to
    specify the exact type of sensor that is connected. Note: the mode must be
    correctly set before setting the sensor type.
    
    Ports can be found at `/sys/class/lego-port/port<N>` where `<N>` is
    incremented each time a new port is registered. Note: The number is not
    related to the actual port at all - use the `port_name` attribute to find
    a specific port.
    """

#~autogen
#~autogen pure-python_generic-get-set classes.legoPort>currentClass


    def __get_driver_name(self):
        return self._device._get_attribute( 'driver_name' )

    __doc_driver_name = (
        "Returns the name of the driver that loaded this device. You can find the"
        "complete list of drivers in the [list of port drivers]."        )

    driver_name = property( __get_driver_name, None, None, __doc_driver_name )

    def __get_modes(self):
        return self._device._get_attribute( 'modes' )

    __doc_modes = (
        "Returns a list of the available modes of the port."        )

    modes = property( __get_modes, None, None, __doc_modes )

    def __get_mode(self):
        return self._device._get_attribute( 'mode' )

    def __set_mode(self, value):
        self._device._set_attribute( 'mode', value )

    __doc_mode = (
        "Reading returns the currently selected mode. Writing sets the mode."
        "Generally speaking when the mode changes any sensor or motor devices"
        "associated with the port will be removed new ones loaded, however this"
        "this will depend on the individual driver implementing this class."        )

    mode = property( __get_mode, __set_mode, None, __doc_mode )

    def __get_port_name(self):
        return self._device._get_attribute( 'port_name' )

    __doc_port_name = (
        "Returns the name of the port. See individual driver documentation for"
        "the name that will be returned."        )

    port_name = property( __get_port_name, None, None, __doc_port_name )

    def __set_set_device(self, value):
        self._device._set_attribute( 'set_device', value )

    __doc_set_device = (
        "For modes that support it, writing the name of a driver will cause a new"
        "device to be registered for that driver and attached to this port. For"
        "example, since NXT/Analog sensors cannot be auto-detected, you must use"
        "this attribute to load the correct driver. Returns -EOPNOTSUPP if setting a"
        "device is not supported."        )

    set_device = property( None, __set_set_device, None, __doc_set_device )

    def __get_status(self):
        return self._device._get_attribute( 'status' )

    __doc_status = (
        "In most cases, reading status will return the same value as `mode`. In"
        "cases where there is an `auto` mode additional values may be returned,"
        "such as `no-device` or `error`. See individual port driver documentation"
        "for the full list of possible values."        )

    status = property( __get_status, None, None, __doc_status )


#~autogen
