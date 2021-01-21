import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

import { IUser } from '../interfaces/user.interface';

@Entity('user')
export class User implements IUser {
  @PrimaryGeneratedColumn()
  id: number

  @Column({ unique: true })
  username: string

  @Column()
  password: string

  @Column({ unique: true })
  email: string

  @Column()
  joinDate: number

  @Column()
  lastDate: number
}