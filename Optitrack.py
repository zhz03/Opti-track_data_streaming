# coding: utf8
#Copyright © 2018 Naturalpoint
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


# OptiTrack NatNet direct depacketization sample for Python 3.x
#
# Uses the Python NatNetClient.py library to establish a connection (by creating a NatNetClient),
# and receive data via a NatNet connection and decode it using the NatNetClient library.

from NatNetClient import NatNetClient
import time
import numpy as np

class OptiTrack():
	"""docstring for Opt"""
	def __init__(self):
		# This will create a new NatNet client
		streamingClient = NatNetClient()
		self.position = np.zeros(3)
		self.rotation = np.zeros(4)
		self.rpy = np.zeros(3)
		self.position_prev = np.zeros(3)
		self.rotation_prev = np.zeros(4)
		self.velocity = np.zeros(3)
		self.rotation_rate = np.zeros(3)

		self.update_time = time.time()

		# Configure the streaming client to call our rigid body handler on the emulator to send data out.
		streamingClient.newFrameListener = self.receiveNewFrame
		streamingClient.rigidBodyListener = self.receiveRigidBodyFrame

		# Start up the streaming client now that the callbacks are set up.
		# This will run perpetually, and operate on a separate thread.
		print("Start motion capture streaming")
		streamingClient.run()

	# This is a callback function that gets connected to the NatNet client and called once per mocap frame.
	def receiveNewFrame(self, frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
						labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
		# print( "Received frame", frameNumber )
		pass

	# This is a callback function that gets connected to the NatNet client. It is called once per rigid body per frame
	def receiveRigidBodyFrame(self, id, position, rotation):
		# print( "Received frame for rigid body", id )
		self.position = self.postition_enu2ned(position)
		self.rotation = self.orientation_enu2ned(rotation)

		current_time = time.time()
		dt = 0.01 # (current_time - self.update_time)
		self.velocity = (self.position - self.position_prev) / dt
		self.rotation_rate = self.omega(self.rotation, self.rotation_prev, dt)

		self.update_time = current_time
		self.position_prev = self.position
		self.rotation_prev = self.rotation

	def postition_enu2ned(self, position):
		return np.array([position[0], position[2], -position[1]]) # north-east-down

	def orientation_enu2ned(self, quaternion):
		# Change order from xyzw to wxyz
		return np.array([quaternion[3], quaternion[0], quaternion[2], -quaternion[1]]) # w, y, x, -z

	def omega(self, quaternion, quaternion_prev, dt):
		dq = (quaternion - quaternion_prev) / dt
		w, x, y, z = quaternion
		omega = 2 * np.mat([[w, x, y, z],
							[-x, w, z, -y],
							[-y, -z, w, x],
							[-z, y, -x, w]]) * np.vstack(dq)
		return np.asarray(omega[1:4]).reshape(-1)

if __name__ == "__main__":
	
	op = OptiTrack()

	current_time = time.time()

	while True:
		pass
		if time.time()-current_time >= 0.1:
			#print('position = %s rotation = %s' % (op.position, op.rotation))
			print('position = %s' % (op.position))
			current_time = time.time()
